// Push Front
// Given an array and an additional value, insert this value at the beginning of the array. You may use .push(), you are able do this without it though!

function pushFront(a, b){
    a.push();
    for (var i = a.length-1; i>=0; i--){
        a[i] = a[i-1];
    }
    a[0]=b
    console.log(a)

}
pushFront([4,5,7,2,5,2], 18)

// OR 

function pushFrontalso(a,b){
    let addVal = [b];
    a = addVal.concat(a);
    return a
}

console.log(pushFrontalso([1,5,7], 27))

//SOLUTION GIVEN: 
function pushFrontSolution(arr, val){
    for (let i=arr.length; i>=0; i--){
        arr[i] = arr[i-1];
    }
    arr[0] = val;
    return arr;
}
console.log("Push Front Solution: ", pushFrontSolution([1,3,4,56,7,8], 13));








// Pop Front
// Given an array, remove and return the value at the beginning of the array. Prove the value is removed from the array by printing it. You may use .pop(), you are able do this without it though!


function removeFront(c){
    var firstVal = c[0];
    for (var i=0; i<c.length; i++){
        c[i] = c[i+1]
    }
    c.pop()
    console.log("new array: ", c)
    return firstVal
}

console.log("First Value Removed: ", removeFront([5,8,7,1,2,25]))

function removeFrontSolution(c){
    var firstVal = c[0];
    for (var i=0; i<c.length; i++){
        c[i] = c[i+1];
    }
    c.length = c.length-1;
    console.log("New rmv frst val array solution: ", c)
    return firstVal
}
console.log("first Val removd Sol: ", removeFrontSolution([3,7,15,94,-35]))



// Insert At
// Given an array, index, and additional value, insert the value into array at given index. You can think of pushFront(arr,val) as equivalent to insertAt(arr,0,val). You may use .push(), you are able do this without it though!

function insertAt(a, i, v){
    a.push(0);
    for (var x=a.length-1; x>i; x--){
        a[x] = a[x-1];
    }
    a[i] = v;
    console.log(a);
}

insertAt([10,20,35,50,78,91,3,-7], 5, 45)






// BONUS: Remove At
// Given an array and an index into array, remove and return the array value at that index. Prove the value is removed from the array by printing it. Think of popFront(arr) as equivalent to removeAt(arr,0).

function removeAt(a, i){
    let ndx = a[i];
    for (var x = i; x<a.length-1; x++){
        a[x] = a[x+1];
    }
    a.pop();
    console.log(a);
    return ndx
}
console.log("the number", removeAt([4,7,3,5,1,9,25,-4,0,8], 4), " was removed.")







// BONUS: Swap Pairs
// Swap positions of successive pairs of values of given array. If length is odd, do not change the final element.

function swapPairs(arr){
    for (var i = 0; i<arr.length-1; i++){
        if (i%2 == 0){
            var temp = arr[i];
            arr[i] = arr[i+1];
            arr[i+1] = temp;
        }
    }
    console.log(arr);
}

swapPairs([5,-8,105,73,-6,4,1])







// BONUS: Remove Duplicates
// Given a sorted array, remove duplicate values. Because array elements are already in order, all duplicate values will be grouped together. If you already made the Remove At function, you are welcome to use that! If you solved this using nested loops, for an extra challenge, try to do it without any nested loops!

function removeDups(arr){
    for (var i=0; i<arr.length-1; i++){
        if (arr[i] == arr[i+1]){
            removeAt(arr, arr[i+1])
        }
    }
    return arr;
}

console.log("New array is: ", removeDups([1,2,3,3,4,5,6,6,7,8,9,9]));