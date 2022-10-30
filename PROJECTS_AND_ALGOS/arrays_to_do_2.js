// REVERSE:
// Given a numerical array, reverse the order of values, in-place. The reversed array should have the same length, with existing elements moved to other indices so that order of elements is reversed. Working 'in-place' means that you cannot use a second 
// array – move values within the array that you are given. As always, do not use built-in array functions such as splice().


function reverse(arr){
    for (var i =0; i< (arr.length-1)/2; i++){
        var temp = arr[i];
        arr[i] = arr[arr.length-(i+1)];
        arr[arr.length-(i+1)] = temp;
        console.log(arr);
    }
}

reverse([6,8,4,5,3,9,15])