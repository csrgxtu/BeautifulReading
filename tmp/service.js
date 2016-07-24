module.exports = {
  GetUserByBook: function(db, bid) {
    return new Promise(function(resolve,reject) {
      var cmd = 'select expand(in(UserHasBook)) from Book where bid = "' + bid + '"';
      db.query(cmd).then(function(data) {
        resolve(data);
      });
    });
  }
};
