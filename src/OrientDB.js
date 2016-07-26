var OrientDB = require('orientjs');

var server = OrientDB({
   host:       '192.168.100.2',
   port:       2424,
   username:   'root',
   password:   'archer'
});

var db = server.use({
  name:     'bookshelf',
  user:     'root',
  password: 'archer'
});

var cmd = 'select from User where user_id="32849571622349cb976259d8ecb56872"'
var hitters = db.query(cmd).then(
    function(users) {
      console.log('debug');
      console.log(users);
    }
);

db.close();
server.close();
