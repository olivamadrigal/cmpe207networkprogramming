var app = require('express')();
var http = require('http').createServer(app);
var io = require('socket.io')(http);


app.get('/', function(req, res) {
    res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
    console.log('a user connected');
    socket.broadcast.emit('a user has just connected :0')
    socket.on('disconnect', function(){
        console.log('user disconnected');
    });
});

io.on('connection', function(socket){
    socket.on('chat message', function(msg) {
        io.emit('chat message', msg);
        console.log('message: ' + msg);
    });
});
io.emit('some event', {for: 'everyone'});
io.on('connection', function(socket){
    socket.broadcast.emit('hi');
});

http.listen(3000, function() {
    console.log('listening on *:3000');
});

