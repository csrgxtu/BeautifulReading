var sys = require('sys');
var jslitmus = require('./jslitmus.js');

var a = new Array(10000);
jslitmus.test('Join 10K elements', function() {
    a.join(' ');
});

// Log the test results
jslitmus.on('complete', function(test) {
    sys.log(test);
});

// Run it!
jslitmus.runAll();
