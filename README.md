# Flask REST API

## Overview
This project is a simple REST API built using Python and Flask. It performs CRUD (Create, Read, Update, Delete) operations on user data stored in an in-memory dictionary.

## Features
- Get all users (GET)
- Get a single user (GET)
- Add a new user (POST)
- Update an existing user (PUT)
- Delete a user (DELETE)

## Technologies Used
- Python
- Flask
- Postman

## Installation

1. Install Flask:
```bash
pip install flask
```

2. Run the application:
```bash
python app.py
```

The server will start at:

```
http://127.0.0.1:5000
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/users` | Get all users |
| GET | `/users/<id>` | Get a specific user |
| POST | `/users` | Add a new user |
| PUT | `/users/<id>` | Update a user |
| DELETE | `/users/<id>` | Delete a user |

## Testing

The API was tested using **Postman**.

## Project Structure

```
flask-rest-api/
│
├── app.py
├── requirements.txt
├── README.md
└── screenshots/
```

## Learning Outcome

- Built a REST API using Flask.
- Learned HTTP methods (GET, POST, PUT, DELETE).
- Worked with JSON data.
- Tested APIs using Postman.

## Author
Sumra Arman