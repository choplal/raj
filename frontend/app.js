const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
app.use(bodyParser.urlencoded({ extended: true }));

// Show form
app.get('/', (req, res) => {
    res.send(`
        <h2>Simple Form</h2>
        <form action="/submit" method="POST">
            <input type="text" name="name" placeholder="Enter name" required/>
            <button type="submit">Submit</button>
        </form>
    `);
});

// Handle form submission
app.post('/submit', async (req, res) => {
    const name = req.body.name;

    try {
        const response = await axios.post('http://backend:5000/api', {
            name: name
        });

        res.send(response.data.message);
    } catch (error) {
        res.send('Error connecting to backend');
    }
});

app.listen(3000, () => console.log('Frontend running on port 3000'));