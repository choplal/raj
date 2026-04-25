from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Backend is running!"

@app.route('/api', methods=['POST'])
def handle_form():
    data = request.json
    name = data.get('name')

    return jsonify({
        "message": f"Hello {name}, data received in backend!"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)