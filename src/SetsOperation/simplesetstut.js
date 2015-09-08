var sets = require('simplesets');

var s1 = new sets.Set(['A', 'B', 'C', 'D']);
var s2 = new sets.Set(['B', 'D', 'C', 'F', 'G', 'I', 'L']);

var s3 = s1.intersection(s2);
console.log(s3.array() + ':' + s3.size());
