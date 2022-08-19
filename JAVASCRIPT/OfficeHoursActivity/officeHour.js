// Guess the output from the function below
function funWithNum(num){
    if (num > 10){
        console.log('Greater than 10');
        return num
    }else{
        console.log('Less than 10');
        return num * 2
    }
}
console.log(funWithNum(4));
funWithNum(200);

//1.) Write a function sayHello that takes in 2 parameters both strings, name and day. Have the function console log "Hello {name} Happy {day}!"
// Example sayHello('Caden', 'Sunday') --> should console log --> "Hello Caden Happy Sunday!"

//2.) Write a function logAllNums to console log all numbers between 1-255 

//3.) Take the function from above and instead of console logging every number add the number to an array then return the array at the end 
// Example of the return [1,2,3,4,5,6,7,8,9,10,.......,255]

//4.) Write a function sumAllNums to sum all numbers from 1 to 100 the function should return the sum at the very end 

//5.) Write another sum function sumEvenNums to sum all EVEN numbers between 1 and 100

//6.) BONUS: write a function highNum that takes 1 parameter which will be an array and returns the highest number in that array 
// Example: highNum([2,34,4,90,-1,20,5]) should return 90 

