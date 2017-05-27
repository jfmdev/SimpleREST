// Import dependencies.
const express = require('express')
const bodyParser = require('body-parser');
const uuidV1 = require('uuid/v1');

// Initialize server.
const app = express()
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

// Define static folder.
app.use(express.static('templates'));
app.use('/lib', express.static('static'))

// Define /ping service.
app.get('/ping', function (req, res) {
    res.json({'success': true, 'data': "pong"});
});

// Define /timestamp service.
app.get('/timestamp', function (req, res) {
    let now = new Date();
    res.json({'success': true, 'data': now});
});

// Define /uuid service.
app.get('/uuid', function (req, res) {
    let guid = uuidV1();
    res.json({'success': true, 'data': guid});
});

// Define /hello service.
app.post('/hello', function (req, res) {
    let msg = 'Hello ' + req.body.name + '!';
    res.json({'success': true, 'data': msg});
});

// Define /multiply service.
app.post('/multiply', function (req, res) {
    let result = req.body.num1 * req.body.num2;
    res.json({'success': true, 'data': result});
});

// Start server.
app.listen(5000, function () {
  console.log('SimpleREST is listening on port 5000!')
})
