console.log("Welcome");

function chooseCity(element){
    console.log(element);
    alert("Loading weather report for  " + element.innerText + "!");
}

var alertBox = document.querySelector("#cookieAlertBox");
function deleteCookieAlert(){
    alertBox.remove();
}

var temps=[ /*pulled temps and converted to intergers */
    [parseInt(document.querySelector("#high-temp0").innerText), parseInt(document.querySelector("#low-temp0").innerText)],
    [parseInt(document.querySelector("#high-temp1").innerText), parseInt(document.querySelector("#low-temp1").innerText)],
    [parseInt(document.querySelector("#high-temp2").innerText), parseInt(document.querySelector("#low-temp2").innerText)],
    [parseInt(document.querySelector("#high-temp3").innerText), parseInt(document.querySelector("#low-temp3").innerText)]
];
var tempsDefault = [    
    [parseInt(document.querySelector("#high-temp0").innerText), parseInt(document.querySelector("#low-temp0").innerText)],
    [parseInt(document.querySelector("#high-temp1").innerText), parseInt(document.querySelector("#low-temp1").innerText)],
    [parseInt(document.querySelector("#high-temp2").innerText), parseInt(document.querySelector("#low-temp2").innerText)],
    [parseInt(document.querySelector("#high-temp3").innerText), parseInt(document.querySelector("#low-temp3").innerText)]
];

var a = [];
var b = [];
for (i=0; i<temps.length; i++){
    for (x=0; x<temps[i].length; x++){
        temps[i][x] = Math.round((temps[i][x]*(9/5)) + 32);
        a.push(temps[i][x]);
    }
}
for (n=0; n<a.length; n+=2){
    b.push([a[n], a[n+1]]);
}
console.log(b);

var tempChosen = document.querySelector("#selector");
var currentChoice = "celsius";
console.log(currentChoice);
function tempSelected(){
    currentChoice = tempChosen.value;
    function changeTemps(){
        if(currentChoice === "fahrenheit"){
            document.querySelector("#high-temp0").innerText= b[0][0] + "°";
            document.querySelector("#low-temp0").innerText = b[0][1] + "°";
            document.querySelector("#high-temp1").innerText= b[1][0] + "°";
            document.querySelector("#low-temp1").innerText = b[1][1] + "°";
            document.querySelector("#high-temp2").innerText= b[2][0] + "°";
            document.querySelector("#low-temp2").innerText = b[2][1] + "°";
            document.querySelector("#high-temp3").innerText= b[3][0] + "°";
            document.querySelector("#low-temp3").innerText = b[3][1] + "°";
        }
        else{
            document.querySelector("#high-temp0").innerText= tempsDefault[0][0] + "°";
            document.querySelector("#low-temp0").innerText = tempsDefault[0][1] + "°";
            document.querySelector("#high-temp1").innerText= tempsDefault[1][0] + "°";
            document.querySelector("#low-temp1").innerText = tempsDefault[1][1] + "°";
            document.querySelector("#high-temp2").innerText= tempsDefault[2][0] + "°";
            document.querySelector("#low-temp2").innerText = tempsDefault[2][1] + "°";
            document.querySelector("#high-temp3").innerText= tempsDefault[3][0] + "°";
            document.querySelector("#low-temp3").innerText = tempsDefault[3][1] + "°";
        }
    }
    changeTemps();
    }
