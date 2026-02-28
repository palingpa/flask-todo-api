# flask-todo-api

Minimal in-memory TODO API with Flask.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

## Endpoints

- `GET /health`
- `GET /todos`
- `POST /todos` JSON `{"title": "..."}`

