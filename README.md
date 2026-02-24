# cs361-image-microservice — CS361 Sprint 2

## Description

This image microservice API returns URLS of random images of a specified amount and query.

The service relies on HTTP and clients request images by using the /photos/random endpoint.

## Communication Contract

Base URL (Will Be Made Live for Production):

- `busy-beavers-random-images-microservice-api.com/`

### Endpoints expect query params and return a JSON object

- Client specifies amount of images to receive and gives an image search query

### Required headers

Service relies on a valid Unsplash Client Id being sent as a header when retrieving images from Unsplash with GET request, client calling on microservice does not need this.

Example:

```
headers = {"Authorization": f"Client-ID {mcMH9y2TjhwZ_oOTkyWv9yaaXIYTZaYk39MZZBuEmHo}"}
```

## Endpoints

### GET /photos/random

Request Example:

```
https://busy-beavers-random-images-microservice-api/?query=cat&amount=5
```

Response Example:

```json
{
  "amount": 5,
  "query": "cat",
  "results": [
    "https://images.unsplash.com/photo-1545529468-42764ef8c85f?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4ODEzODd8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzE5MDkzNzJ8&ixlib=rb-4.1.0&q=85",
    "https://images.unsplash.com/photo-1574231164645-d6f0e8553590?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4ODEzODd8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzE5MDkzNzJ8&ixlib=rb-4.1.0&q=85",
    "https://images.unsplash.com/photo-1584290867415-527a8475726d?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4ODEzODd8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzE5MDkzNzJ8&ixlib=rb-4.1.0&q=85",
    "https://images.unsplash.com/photo-1595752776689-aebef37b5d32?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4ODEzODd8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzE5MDkzNzJ8&ixlib=rb-4.1.0&q=85",
    "https://images.unsplash.com/photo-1612532275214-e4ca76d0e4d1?crop=entropy&cs=srgb&fm=jpg&ixid=M3w4ODEzODd8MHwxfHJhbmRvbXx8fHx8fHx8fDE3NzE5MDkzNzJ8&ixlib=rb-4.1.0&q=85"
  ]
}
```

## UML Sequence Diagram

![UML Diagram](./uml-image-microservice.png)

\_Figure 1. UML Sequence for the image microservice
