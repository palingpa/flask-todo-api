from flask import Flask, jsonify, request

app = Flask(__name__)

todos = []
_next_id = 1


@app.get("/health")
def health():
    return jsonify({"ok": True})


@app.get("/todos")
def list_todos():
    return jsonify(todos)


@app.post("/todos")
def create_todo():
    global _next_id
    data = request.get_json(silent=True) or {}
    title = (data.get("title") or "").strip()
    if not title:
        return jsonify({"error": "title required"}), 400
    item = {"id": _next_id, "title": title, "done": False}
    _next_id += 1
    todos.append(item)
    return jsonify(item), 201


@app.patch("/todos/<int:todo_id>")
def update_todo(todo_id):
    data = request.get_json(silent=True) or {}
    for item in todos:
        if item["id"] == todo_id:
            if "title" in data:
                title = (data.get("title") or "").strip()
                if not title:
                    return jsonify({"error": "title required"}), 400
                item["title"] = title
            if "done" in data:
                item["done"] = bool(data["done"])
            return jsonify(item)
    return jsonify({"error": "not found"}), 404


@app.delete("/todos/<int:todo_id>")
def delete_todo(todo_id):
    for i, item in enumerate(todos):
        if item["id"] == todo_id:
            todos.pop(i)
            return "", 204
    return jsonify({"error": "not found"}), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)

