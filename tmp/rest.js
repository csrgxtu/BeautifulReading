var orientdb = require('node-orientdb-http');
var uniq = require("uniq");
var SyncPromise = require('sync-promise');
var Service = require('./service');

var db = orientdb.connect({
    host: "http://192.168.100.2:2480",
    user: "root",
    password: "archer",
    database: "bookshelf"
});

db.on('connect', function() {
    // yes! connected
    console.log('connected');
});

db.on('error', function(err) {
    // mmm error ..
    console.log(err);
});



function successHandler(data) {
  // console.log(data);
  for (var i = 0; i < data.result.length; i++) {
    Books.push(data.result[i].bid);
  }
  Books = uniq(Books);
  // console.log(Books);

  for (var i = 0; i < Books.length; i++) {
    // cmd = 'select expand(in(UserHasBook)) from Book where bid = "' + data.result[i].bid + '"';
    var rtv = Func(db, Books[i]);
    console.log(rtv.finally(function(){
      console.log(rtv.isPending);
    }));
    // db.query(cmd).then(function(data) {
    //   console.log(data);
    // });
    console.log('what');
  }
  console.log('daye');
}

function errorHandler(err) {
  console.log(err);
}

var Books = [];
var Users = {};
var Func = Service.GetUserByBook;
// var GetUserByBook = function(bid) {
//   return new Promise(function(resolve,reject) {
//     var cmd = 'select expand(in(UserHasBook)) from Book where bid = "' + bid + '"';
//     db.query(cmd).then(function(data) {
//       resolve(data);
//     });
//   });
// };

console.log(Service.GetUserByBook);
var cmd = 'select expand(out(UserHasBook)) from  #26:436;'
db.query(cmd).then(successHandler, errorHandler);
