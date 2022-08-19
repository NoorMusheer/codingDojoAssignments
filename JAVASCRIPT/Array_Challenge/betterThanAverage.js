

function betterThanAverage(arr) {
    var sum = 0;
    // calculate the average
    for (i=0; i<arr.length; i++){
        sum = sum + arr[i];
    }
    console.log(sum);
    var avg = sum / arr.length;
    console.log(avg);
    var count = 0;
    for (a=0; a<arr.length; a++){
        if (arr[a]>avg){
            count = count +1;
        }
    }
    // count how many values are greated than the average
    return count;
}
var result = betterThanAverage([6, 8, 3, 10, -2, 5, 9]);
console.log(result); // we expect back 4
