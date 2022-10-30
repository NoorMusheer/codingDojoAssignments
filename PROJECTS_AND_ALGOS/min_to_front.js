// Given an array of comparable values, move the lowest element to array’s front, shifting backward any elements previously ahead of it. Do not otherwise change the array’s order. Given [4,2,1,3,5], change it to [1,4,2,3,5] and return it. As always, do this without using built-in functions.


function minToFront(arr){
    var min = arr[0];
    var index = 0;
    for (var i=0; i<arr.length-1; i++){
        if (arr[i] < min) {
            min = arr[i];
            index = i;
        };
    };
    for (var i=index; i>=0; i--){
        arr[i] = arr[i-1];
    }
    arr[0] = min;
    console.log(arr);

}
minToFront([4,2,1,3,5,-100,1580,3,-3])