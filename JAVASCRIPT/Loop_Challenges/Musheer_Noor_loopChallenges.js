/*
Print odds 1-20
Using a loop write code that will console.log all of the odd values from 1 up to 20.
*/
function odds(){
    for (var i=0; i<21; i++){
        if (i%2 !=0){
            console.log(i);
        }
    }
}
odds();


/*Decreasing Multiples of 3
Using a loop write code that will console.log all of the values that are evenly divisible by 3 from 100 down to 0.
*/
function divByThree(){
    for (var i=100; i>=0; i--){
        if(i%3==0){
            console.log(i)
        }
    }
}
divByThree();


/*Print the sequence
Using a loop write code that will console.log the values in this sequence 4, 2.5, 1, -0.5, -2, -3.5.
*/

function logValues(arr){
    for (var i=0; i<arr.length; i++){
        console.log(arr[i])
    }
}
logValues([4,2.5,1,-.05,-2,-3.5]);

/*
Sigma
Write code that will add all of the values from 1-100 onto some variable sum and at the end console.log the result 1 + 2 + 3 + ... + 98 + 99 + 100. We should get back 5050 at the end.
*/

var sum = 0; 
function addEmUp(){
    for (var i=0; i<101; i++){
        sum = sum + i;
    }
    return(sum);
}
console.log(addEmUp());



/*
Factorial
Write code that will multiply all of the values from 1-12 onto some variable product and at the end console.log the result 1 * 2 * 3 * ... * 10 * 11 * 12. We should get back 479001600 at the end.
*/

var product = 1;
function multiply(){
    for (i=1; i<13; i++){
        product = product*i;
    }
    return(product);
}
console.log(multiply());

