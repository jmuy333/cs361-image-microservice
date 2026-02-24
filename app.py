from flask import Flask, request, jsonify
import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

UNSPLASH_KEY = os.getenv("UNSPLASH_KEY")

cache = {}
CACHE_EXPIRATION_SECONDS = 300

@app.route("/search", methods=["GET"])
def search():

    # Get query parameters
    query = request.args.get("query")
    amount = request.args.get("amount", 5)

    # Validate query
    if not query:
        return jsonify({
            "error": "query parameter is required"
        }), 400

    # Validate amount
    try:
        amount = int(amount)
    except ValueError:
        return jsonify({
            "error": "amount must be an integer"
        }), 400
    
    # Create cache key
    cache_key = f"{query}-{amount}"

    current_time = time.time()

    # Check Cache First
    if cache_key in cache:
        cached_entry = cache[cache_key]

        # Check expiration
        if current_time - cached_entry["timestamp"] < CACHE_EXPIRATION_SECONDS:
            return jsonify({
                "query": query,
                "amount": amount,
                "results": cached_entry["data"],
                "cached": True
            })

    # Build Unsplash API request
    url = "https://api.unsplash.com/search/photos"
    headers = {
        "Authorization": f"Client-ID {UNSPLASH_KEY}"
    }
    params = {
        "query": query,
        "per_page": amount
    }

    # Call Unsplash
    response = requests.get(url, headers=headers, params=params)

    # Handle API failure
    if response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch images from Unsplash"
        }), 500

    data = response.json()

    # Extract full resolution image URLs
    image_urls = []
    for photo in data["results"]:
        image_urls.append(photo["urls"]["full"])

    cache[cache_key] = {
        "timestamp": current_time,
        "data": image_urls
    }

    # Return structured JSON
    return jsonify({
        "query": query,
        "amount": amount,
        "results": image_urls,
        "cached": False
    })


if __name__ == "__main__":
    app.run(debug=True)