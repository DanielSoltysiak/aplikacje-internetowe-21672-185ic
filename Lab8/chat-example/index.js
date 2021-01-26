const app = require('express')();
const http = require('http').createServer(app);
const io = require('socket.io')(http);

// gdy otworzymy stronę startową app odpowie plikiem podanym w res.send
app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
  });


io.on('connection', (socket) => {
  socket.on('chat message', msg => {
    io.emit('chat message', msg);
  });
});

// server http nasłuchuje na porcie 3000
http.listen(3000, () => {
  console.log('listening on *:3000');
});

