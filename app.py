from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://rajsh0969_db_user:VCk3MxNQtls1f92U@cluster0.u1imnxu.mongodb.net/choplaldb?retryWrites=true&w=majority")

db = client["choplaldb"]
collection = db["users"]

import json

@app.route('/api')
def api():
    with open('data.json') as f:
        data = json.load(f)
    return data

@app.route('/')
def home():
    return '''
    <h2>Submit Form</h2>
    <form method="POST" action="/submit">
        Name: <input name="name" required><br><br>
        Email: <input name="email" required><br><br>
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        collection.insert_one({
            "name": name,
            "email": email
        })

        return "Data submitted successfully"

    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
print("Server is running on http://localhost:5000")