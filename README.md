# Recipe Manager API

*A REST API built with FastAPI, SQLAlchemy, and SQLite*

---

## Overview

The Recipe Manager API is a fully functional REST API that allows users to create, view, update, delete, and filter recipes. Each recipe stores a title, description, ingredients, instructions, and a category tag. All data persists in a local SQLite database.

---

## Features

- Full CRUD operations on recipes
- Filter recipes by category via query parameter
- SQLite database with SQLAlchemy ORM
- Pydantic schema validation on all inputs and outputs
- Proper HTTP status codes (201 Created, 204 No Content, 404 Not Found)
- Auto-generated interactive API docs via Swagger UI at `/docs`

---

## Tech Stack

- **FastAPI** — web framework and routing
- **SQLAlchemy** — ORM and database management
- **SQLite** — local database file
- **Pydantic** — request and response validation
- **Uvicorn** — ASGI server

---

## Project Structure

```
RecipeManager/
├── main.py              # App entry point, router registration
├── database.py          # Database connection and session
├── models.py            # SQLAlchemy Recipe model
├── schemas.py           # Pydantic schemas for validation
└── routers/
    └── recipes.py       # Recipe CRUD endpoints
```

---

## Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/RecipeManager.git
cd RecipeManager
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install "fastapi[standard]" sqlalchemy
```

### 4. Run the application

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`

Interactive documentation available at `http://127.0.0.1:8000/docs`

The SQLite database file (`recipes.db`) will be created automatically on first run.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/recipes/` | Create a new recipe (201 Created) |
| GET | `/recipes/` | List all recipes (optional `?category=` filter) |
| GET | `/recipes/{id}` | Get a single recipe by ID |
| PUT | `/recipes/{id}` | Update a recipe (partial updates supported) |
| DELETE | `/recipes/{id}` | Delete a recipe (204 No Content) |

---

## Recipe Object

When creating or updating a recipe, the following fields are accepted:

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `title` | string | Yes | The recipe name |
| `description` | string | No | A short summary |
| `ingredients` | string | Yes | Full ingredients list |
| `instructions` | string | Yes | Step-by-step method |
| `category` | string | No | e.g. breakfast, dinner |

---

## Usage Example

Filter recipes by category:

```
GET /recipes/?category=breakfast
```

Partially update a recipe (only send the fields you want to change):

```
PUT /recipes/1
{"title": "Updated Title"}
```

All endpoints can be tested interactively via the Swagger UI at `/docs`.

---

> This project was built as a portfolio piece to demonstrate FastAPI, SQLAlchemy, CRUD operations, and REST API design fundamentals.
