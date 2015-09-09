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

function array_intersect() {
  var i, all, shortest, nShortest, n, len, ret = [], obj={}, nOthers;
  nOthers = arguments.length-1;
  nShortest = arguments[0].length;
  shortest = 0;
  for (i=0; i<=nOthers; i++){
    n = arguments[i].length;
    if (n<nShortest) {
      shortest = i;
      nShortest = n;
    }
  }

  for (i=0; i<=nOthers; i++) {
    n = (i===shortest)?0:(i||shortest); //Read the shortest array first. Read the first array instead of the shortest
    len = arguments[n].length;
    for (var j=0; j<len; j++) {
        var elem = arguments[n][j];
        if(obj[elem] === i-1) {
          if(i === nOthers) {
            ret.push(elem);
            obj[elem]=0;
          } else {
            obj[elem]=i;
          }
        }else if (i===0) {
          obj[elem]=0;
        }
    }
  }
  return ret;
}

function array_big_intersect () {
  var args = Array.prototype.slice.call(arguments),
      aLower = [],
      aStack = [],
      count,
      i,
      nArgs,
      nLower,
      oRest = {},
      oTmp = {},
      value,
      compareArrayLength = function (a, b) {
        return (a.length - b.length);
      },
      indexes = function (array, oStack) {
        var i = 0,
            value,
            nArr = array.length,
            oTmp = {};

        for (; nArr > i; ++i) {
          value = array[i];
          if (!oTmp[value]) {
            oStack[value] = 1 + (oStack[value] || 0); // counter
            oTmp[value] = true;
          }
        }

        return oStack;
      };

  args.sort(compareArrayLength);
  aLower = args.shift();
  nLower = aLower.length;

  if (0 === nLower) {
    return aStack;
  }

  nArgs = args.length;
  i = nArgs;
  while (i--) {
    oRest = indexes(args.shift(), oRest);
  }

  for (i = 0; nLower > i; ++i) {
    value = aLower[i];
    count = oRest[value];
    if (!oTmp[value]) {
      if (nArgs === count) {
        aStack.push(value);
        oTmp[value] = true;
      }
    }
  }

  return aStack;
}
