from flask import Flask, request, jsonify
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = Flask(__name__)

UNSPLASH_KEY = os.getenv("UNSPLASH_KEY")


@app.route("/photos/random", methods=["GET"])
def random_photos():
    
     # Get query parameters
    query = request.args.get("query")
    amount = request.args.get("amount", 5)

    # Validate query
    if not query:
        return jsonify({"error": "query parameter is required"}), 400

    # Validate amount
    try:
        amount = int(amount)
    except ValueError:
        return jsonify({"error": "amount must be an integer"}), 400

    # Build Unsplash API request
    url = "https://api.unsplash.com/photos/random"
    headers = {"Authorization": f"Client-ID {UNSPLASH_KEY}"}
    params = {"query": query, "count": amount}

    # Call Unsplash
    response = requests.get(url, headers=headers, params=params)

    # Handle API failing
    if response.status_code != 200:
        return jsonify({
            "error": "Failed to fetch images from Unsplash",
            "status_code": response.status_code
        }), 500

    data = response.json()

    # Extract full resolution image URLs
    image_urls = [photo["urls"]["full"] for photo in data]

    # Return structured JSON
    return jsonify({
        "query": query,
        "amount": amount,
        "results": image_urls
    })


if __name__ == "__main__":
    app.run(debug=True)