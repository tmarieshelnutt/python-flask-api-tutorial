from flask import Flask, jsonify
from flask import request

todos = [
    { "label": "My second task", "done": False }
]

app = Flask(__name__)


@app.route('/todos', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.get_json(force=True)
    # print("Incoming request with the following body", request_body)
    if request_body:
        todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if todos:
        todos.pop(position)
    return jsonify(todos)


# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)