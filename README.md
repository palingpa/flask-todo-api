# flask-todo-api

Minimal in-memory TODO API with Flask. Data resets when the process exits.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

## Endpoints

| Method | Path | Body |
|--------|------|------|
| GET | `/health` | — |
| GET | `/todos` | — |
| POST | `/todos` | `{"title": "..."}` |
| PATCH | `/todos/<id>` | `{"title"?: "...", "done"?: bool}` |
| DELETE | `/todos/<id>` | — |

## Example

```bash
curl -X POST localhost:5000/todos -H 'Content-Type: application/json' -d '{"title":"buy milk"}'
curl localhost:5000/todos
```


## License

MIT
