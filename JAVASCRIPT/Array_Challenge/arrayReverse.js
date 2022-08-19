
function reverse(arr) {
    var revArray = [];
    for (i=arr.length-1; i>=0; i--){
        revArray.push(arr[i]);
    }
    return (revArray);
}
   
var result = reverse(["a", "b", "c", "d", "e"]);
console.log(result); // we expect back ["e", "d", "c", "b", "a"]
