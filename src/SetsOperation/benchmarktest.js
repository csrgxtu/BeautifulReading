var sys = require('sys');
var jslitmus = require('./jslitmus/jslitmus.js');
var sets = require('simplesets');

// 使用别人实现的库
/**
 * intersection
 * get the length of the intersection sets of two array
 *
 * @param array1
 * @param array2
 * @return int
 */
function intersection(array1, array2) {
  var s1 = new sets.Set(array1);
  var s2 = new sets.Set(array2);

  var s3 = s1.intersection(s2);

  // here return the length
  return s3.size();
}

// 遍历的方法
// 对于第一个数组中的每个元素，检查是否在第二个数组中
/**
 * intersectiona
 * get the length of the intersection sets of two array
 *
 * @param array1
 * @param array2
 * @return int
 */
function intersectiona(array1, array2) {
  var counter = 0;

  if (array1.length == 0 || array2.length == 0) {
    return counter;
  }

  for (var i = 0; i < array1.length; i++) {
    if (array2.indexOf(array1[i]) >= 0) {
      counter = counter + 1;
    }
  }

  return counter;
}

/**
 * union
 * get the length of the union sets of two array
 *
 * @param array1
 * @param array2
 * @return int
 */
function union(array1, array2) {
  var s1 = new sets.Set(array1);
  var s2 = new sets.Set(array2);

  var s3 = s1.union(s2);

  return s3.size();
}

// 遍历方法， 将第二个数组中的元素无重复的加入第一个数组
/**
 * uniona
 * get the length of the union sets of two array
 *
 * @param array1
 * @param array2
 * @return int
 */
function uniona(array1, array2) {
  if (array1.length == 0 && array2.length == 0) {
    return 0;
  }

  for (var i = 0; i < array2.length; i++) {
    if (array1.indexOf(array2[i]) < 0) {
      array1.push(array2[i]);
    }
  }

  return array1.length;
}


var array1 = ['A', 'B', 'C', 'D'];
var array2 = ['B', 'D', 'C', 'F', 'G', 'I', 'L'];

jslitmus.test('INTERSECTION', function cb() {
  intersection(array1, array2);
});

jslitmus.test('INTERSECTIONA', function cb() {
  intersectiona(array1, array2);
  // intersection(array1, array2);
});

jslitmus.test('UNION', function cb() {
  union(array1, array2);
});

jslitmus.test('UNIONA', function cb() {
  uniona(array1, array2);
});


// Log the test results
jslitmus.on('complete', function(test) {
    sys.log(test);
});

// Run it!
jslitmus.runAll();
// jslitmus.Test.run(1000, true);
