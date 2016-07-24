var OrientDB = require('orientjs');

var server = OrientDB({
   host:       '192.168.100.2',
   port:       2424,
   username:   'root',
   password:   'archer'
});
var db = server.use('bookshelf');

var cmd = 'select from User where user_id="32849571622349cb976259d8ecb56872"'
var hitters = db.query(cmd);
console.log(hitters);

db.close();
server.close();
