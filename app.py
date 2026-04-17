from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import json

app = Flask(__name__)

client = MongoClient("mongodb+srv://rajsh0969_db_user:VCk3MxNQtls1f92U@cluster0.u1imnxu.mongodb.net/choplaldb?retryWrites=true&w=majority")

db = client["choplaldb"]
collection = db["users"]


# ---------------- API ----------------
@app.route('/api', methods=['GET'])
def api():
    try:
        with open('data.json') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})


# ---------------- HOME PAGE ----------------
@app.route('/')
def home():
    return '''
    <h2>Submit Form</h2>
    <form method="POST" action="/submit">
        Name: <input name="name" required><br><br>
        Email: <input name="email" required><br><br>
        <button type="submit">Submit</button>
    </form>

    <br>
    <a href="/todo">Go to To-Do Form</a>
    '''


# ---------------- SHOW TODO HTML ----------------
@app.route('/todo')
def todo():
    return render_template("todo.html")


# ---------------- SUBMIT USER ----------------
@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "type": "user",
            "name": name,
            "email": email
        })

        return "User data submitted successfully"

    except Exception as e:
        return f"Error: {str(e)}"


# ---------------- SUBMIT TODO ----------------
@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
    try:
        item = {
            "type": "todo",
            "itemName": request.form['itemName'],
            "itemDescription": request.form['itemDescription'],
            "itemId": request.form['itemId'],
            "itemUUID": request.form['itemUUID'],
            "itemHash": request.form['itemHash']
        }

        collection.insert_one(item)

        return "To-do item added successfully"

    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)
