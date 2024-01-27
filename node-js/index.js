var http = require('http');
var dt = require('./out');
var fs = require('fs');

http.createServer(function (req, res) {
  res.writeHead(200, {'Content-Type': 'text/html'});
  res.write("The date and time are currently: " + dt.myDateTime() + '\n');
  res.end('Hello World! ' + req.url);
}).listen(8080);