/*
//#1//
function sayHello(name, day){
    console.log("Hello " + name + " happy " + day);
}
sayHello("Caden","Sunday");


//#2//
function logAllNums(){
    for (var i=1; i<255; i++){
        console.log(i);
    }
}
logAllNums();
*/


//#3//
function logAllNums(){
    var newArray=[];
    for (var i=1; i<255; i++){
        newArray.push(i);
    }
    return newArray;
};
console.log(logAllNums());
