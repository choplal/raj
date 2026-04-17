from flask import Flask, request, redirect
from pymongo import MongoClient
from flask import render_template

app = Flask(__name__)

client = MongoClient("mongodb+srv://rajsh0969_db_user:VCk3MxNQtls1f92U@cluster0.u1imnxu.mongodb.net/choplaldb?retryWrites=true&w=majority")

db = client["choplaldb"]
collection = db["users"]

import json

@app.route('/todo')
def todo():
    return '''
    <h2>Add To-Do Item</h2>
    <form method="POST" action="/submittodoitem">
        Item Name: <input name="itemName" required><br><br>
        Item Description: <input name="itemDescription" required><br><br>
        <button type="submit">Submit</button>
    </form>
    '''

@app.route('/submittodoitem', methods=['POST'])
def submit_todo():
    try:
        item_name = request.form['itemName']
        item_desc = request.form['itemDescription']

        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_desc
        })

        return "To-Do item saved successfully"

    except Exception as e:
        return f"Error: {str(e)}"

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