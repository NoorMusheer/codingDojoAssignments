
var displayDiv = document.querySelector("#display");
var firstNum = 0;
var operator = "";
var secNum = 0;
var result = 0;
function press(element){
    if (operator == ""){
        if (displayDiv.innerText == 0){
            displayDiv.innerText = element
        }
        else{
            displayDiv.innerText = displayDiv.innerText + element;
        }
    }
    else {
        if (displayDiv.innerText == firstNum){
            displayDiv.innerText = element
        }
        else{
            displayDiv.innerText = displayDiv.innerText + element;
        }
    }
}

function setOP(op){
    operator = op;
    firstNum = parseInt(displayDiv.innerText);
}

function calculate(){
    secNum = parseInt(displayDiv.innerText);
    if (operator == "+"){
        result = firstNum + secNum;
    }
    else if(operator == "-"){
        result= firstNum - secNum;
    }
    else if(operator == "*"){
        result= firstNum * secNum;
    }
    else if(operator == "/"){
        result= firstNum / secNum;
    }
    displayDiv.innerText = result;
    firstNum = 0;
    secNum =0;
    operator = "";
    result = 0;

}

function clr(){
    displayDiv.innerText = 0;
    firstNum = 0;
    secNum =0;
    operator = "";
}







