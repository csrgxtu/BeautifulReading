var express = require('express');
var ParseDashboard = require('parse-dashboard');

var dashboard = new ParseDashboard({
  "apps": [
    {
      "serverURL": "http://192.168.100.2:9600/parse",
      "appId": "appid",
      "masterKey": "masterKey",
      "clientKey": "clientKey",
      "appName": "br",
      "production": true
    }
  ]
});

var app = express();

// make the Parse Dashboard available at /dashboard
app.use('/dashboard', dashboard);

var httpServer = require('http').createServer(app);
httpServer.listen(9601);
console.log("dashboard on 9601");
