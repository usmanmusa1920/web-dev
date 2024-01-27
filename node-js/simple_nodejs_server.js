const rl = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
  });
  
  rl.question('Who are you? : ', name => {
    console.log(`Hey there ${name}, your server is live...`);
    rl.close();
  })

tab = require('./my_js')

var http = require('http');
var dt = Date()

// console.log(`Hellow world ${dt} ${tab}`);

http.createServer(function (req, res){
    res.writeHead(200, {'content-Type': 'text/html'});
    // res.write('who');
    res.write(req.url);
    res.end();
    // res.end(`Hellow world, the current time is =>> ${dt} ${tab}`);
}).listen(8080);
