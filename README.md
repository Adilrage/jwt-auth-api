# JWT Authentication API

A RESTful authentication API built with FastAPI, SQLAlchemy, SQLite, Passlib and JWT.

## Features

- User registration
- User login
- Password hashing using bcrypt
- JWT authentication
- Protected profile endpoint
- SQLite database
- Swagger API documentation

## Technologies

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Passlib
- python-jose
- Uvicorn

## Installation

Install the required packages:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
uvicorn app.main:app --reload
```

Open the Swagger documentation:

```
http://127.0.0.1:8000/docs
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home endpoint |
| POST | /register | Register a new user |
| POST | /login | Authenticate a user and generate a JWT token |
| GET | /profile | Protected endpoint |

## Author

Adil Rage
