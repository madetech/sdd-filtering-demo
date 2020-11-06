const serverless = require('serverless-http');
const express = require('express')
const app = express()

app.get('/', function (req, res) {
    console.log(arguments);
    res.send('Hello World!1!1')
})

module.exports.handler = serverless(app);
