//simulate a queue, remove index 0 and add new item to the array
function next(arr, item){
    arr.push(item);
    return arr.shift();

}

var testArr = [1,2,3,4,5];

console.log("Before: " + JSON.stringify(testArr));
console.log(next(testArr, 6))
console.log("After: " + JSON.stringify(testArr));