var http = require('http').createServer(handler);
var fs = require('fs');
// var io = require('socket.io')(http)

const UdpListenPort = 3000;
const RemoteAddress2 = '127.0.0.1'
const UdpTransmitPort2 = 3001;

const io = require('socket.io')(http, {
  cors: {
    origin: "http://localhost:8080",
    methods: ["GET", "POST"],
    transports: ['websocket', 'polling'],
    credentials: true
  },
  allowEIO3: true
});

http.listen(8080, () => {
  console.log("listening");
});

function handler(req, res) {
  fs.readFile('index.html', function (err, data) {
    if (err) {
      res.writeHead(404, { 'Content-Type': 'text/html' });
      return res.end("404 Not Found");
    }
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write(data);
    return res.end();
  });
}
io.sockets.on('connection', (socket) => {
  socket.on('pressed', (arg) => {
    console.log(arg);
    Send2ComLink(arg);
  })
})

var buffer = require('buffer');
const dgram = require('dgram');
const ComLink = dgram.createSocket('udp4');

process.on('SIGINT', function () { //on ctrl+c
  process.exit(); //exit completely
}); 

ComLink.on('error', (err) => {
  console.log(`ComLink udp socket error:\n${err.stack}`);
  ComLink.close();
});

ComLink.on('listening', function () {
  const address = ComLink.address();
  console.log(`Pi is listening to UDP Port ${address.address}:${address.port}:${address.family}`);
  console.log("Pi is transmitting on UDP Port " + RemoteAddress2 + ":" + UdpTransmitPort2);
});

ComLink.on('close', function () {
  console.log('ComLink UDP socket is closed!');
});

ComLink.bind(UdpListenPort);

function Send2ComLink(data) {
  ComLink.send(data + "\n", UdpTransmitPort2, RemoteAddress2, function (error) {
    if (error) {
      ComLink.close();
      console.log('There was an error sending data to ComLink2');
    } else {
      console.log('ComLink2 Data sent: ' + data);
    }
  });
}
