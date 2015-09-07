var koa = require('koa');
var route = require('koa-route');
var koa = require('koa');

var app = koa();

var root = '/home/archer/Documents/BeautifulReading/src/Kong-Dashboard-Koa';
var opts = {
  index: '/public/index.html'
}

app.use(require('koa-static')(root, opts));

app.use(route.get('/', index));
app.use(route.get('/about', about));

function *index() {
 this.body = "<h1>Hello! This is my home page!</h1>";
}

function *about() {
 this.body = "<h2>My name is Adam and I like JavaScript</h2>";
}

app.listen(8008);
console.log('Koa listening on port 8008');
