from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    data = request.get_json(force=True)  #IMPORTANTE APRENDER en producción usar silent=True
    todos.append(data)
    return jsonify(todos), 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    
    print("This is the position to delete:", position)

    if 0 <= position < len(todos):
        todos.pop(position)
    else:
        print("Index out of range")  # print para debugear 


    return jsonify(todos), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)