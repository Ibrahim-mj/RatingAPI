# Menu Item Rating API

This is a REST API that allows authenticated users to rate a menu item and view the available ratings.

## Requirements
Check the requirements.txt file for the required dependencies.

## Installation

1. Clone the repository:
 ```bash
git clone https://github.com/Ibrahim-mj/RatingAPI.git
```
2. Create a virtual environment:
```bash
python -m venv .venv
```
3. Activate the virtual environment:
4. Install the requirements:
```bash
pip install -r requirements.txt
```
5. Run the migrations:
```bash
python manage.py migrate
```
6. Run the server:
```bash
python manage.py runserver
```
7. Open the browser and go to the local server address

## Usage
1. Create a rating:
```bash
POST /api/ratings/
```
Request body:
```json
{
    "menu_id": 1,
    "rating": 5
}
```
Response body:
```json
{
    "id": 1,
    "menu_id": 1,
    "rating": 5,
    "user": 1
}
```
This endpoint uses Djoser's Token Authentication. To get a token, you must register a user and then login. The token is returned in the response body.

2. Register a user:
```bash
POST /auth/users/
```
Request body:
```json
{
    "username": "username",
    "password": "password"
}
```
Response body:
```json
{
    "email": "",
    "username": "username",
    "id": 1
}
```
3. Login:
```bash
POST /auth/token/login/
```
Request body:
```json
{
    "username": "username",
    "password": "password"
}
```
Response body:
```json
{
    "auth_token": "token"
}
```
4. Get all ratings:
```bash
GET /api/ratings/
```
Response body:
```json
[
    {
        "id": 1,
        "menu_id": 1,
        "rating": 5,
        "user": 1
    },
    {
        "id": 2,
        "menu_id": 1,
        "rating": 4,
        "user": 2
    }
]
```
5. Get a rating:
```bash
GET /api/ratings/<id>/
```
Response body:
```json
{
    "id": 1,
    "menu_id": 1,
    "rating": 5,
    "user": 1
}
```

