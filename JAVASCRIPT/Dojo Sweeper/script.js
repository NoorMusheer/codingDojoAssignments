var theDojo = [[1, 0, 1, 1, 1, 0, 4, 0, 8, 0],
[3, 1, 0, 7, 0, 0, 6, 0, 8, 8],
[5, 0, 7, 0, 3, 6, 6, 6, 0, 0],
[2, 3, 0, 9, 0, 0, 6, 0, 8, 0],
[6, 0, 3, 3, 0, 2, 0, 3, 0, 4],
[0, 0, 3, 3, 0, 0, 2, 2, 3, 0],
[0, 0, 0, 0, 5, 0, 1, 2, 0, 6],
[2, 2, 2, 2, 0, 7, 1, 1, 1, 0],
[5, 2, 0, 2, 0, 0, 0, 1, 1, 2],
[9, 2, 2, 2, 0, 7, 0, 1, 1, 0]];
var dojoDiv = document.querySelector("#the-dojo");

// Creates the rows of buttons for this game
function render(theDojo) {
    var result = "";
    for (var i = 0; i < theDojo.length; i++) {
        for (var j = 0; j < theDojo[i].length; j++) {
            result += `<button class="tatami" onclick="howMany(${i}, ${j}, this)"></button>`;
        }
    }
    return result;
}

function randomNinjas(){
    for (var newRows=0; newRows<theDojo.length; newRows++){
        for (var newCols=0; newCols<theDojo[newRows].length; newCols++){
            theDojo[newRows][newCols] = 0; //this changed each value in the field to 0.
        }
    }
    var count = 0; 
    function newCoordinates(){
        var newi = Math.floor(Math.random()*theDojo.length);       //this will be the new i position
        var newj = Math.floor(Math.random()*theDojo[0].length);   //this will be the new j possion
        console.log(newi);
        console.log(newj);
        if (theDojo[newi][newj] == 0){
            theDojo[newi][newj] = 1;
            count = count +1;
        }
    }
    while (count<10){
        newCoordinates();
    }
}
randomNinjas();


// TODO - Make this function tell us how many ninjas are hiding 
//        under the adjacent (all sides and corners) squares.
//        Use i and j as the indexes to check theDojo.
function howMany(i, j, element) {
    console.log({ i, j });

    let a,b,c,m,n,x,y,z = "";

    if (i==0){
        a = b = c = 0;
        x = theDojo[i+1][j-1];
        y = theDojo[i+1][j];
        z = theDojo[i+1][j+1];
    }
    else if (i == theDojo.length-1){
        x = y = z = 0;
        a = theDojo[i-1][j-1];
        b = theDojo[i-1][j];
        c = theDojo[i-1][j+1];
    }
    else if (j==0){
        a = m = x = 0;
        x = theDojo[i+1][j-1];
        y = theDojo[i+1][j];
        z = theDojo[i+1][j+1];
    }
    else if (j == theDojo[0].length-1){
        c = n = z = 0;
        a = theDojo[i-1][j-1];
        b = theDojo[i-1][j];
        c = theDojo[i-1][j+1];
    }
    else {
    a = theDojo[i-1][j-1];
    b = theDojo[i-1][j];
    c = theDojo[i-1][j+1];
    m = theDojo[i][j-1];
    n = theDojo[i][j+1];
    x = theDojo[i+1][j-1];
    y = theDojo[i+1][j];
    z = theDojo[i+1][j+1];
    }
    
    var arrayAround = [
        a,b,c,m,n,x,y,z
    ];
    var totalNinjasAround = 0;
    for (n=0; n<arrayAround.length; n++){
        if(arrayAround[n]>0){
            totalNinjasAround = totalNinjasAround + parseInt(arrayAround[n]);
            
        };
    }
    
    element.innerText = totalNinjasAround;
    
    if (theDojo[i][j] == 1){
        alert("OH NO!! You landed on a ninja! Please play again. " );
        dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`
    }
    //alert("There are " + totalNinjasAround + " ninjas around you right now.");

}

// BONUS CHALLENGES
// 1. draw the number onto the button instead of alerting it
// 2. at the start randomly place 10 ninjas into theDojo with at most 1 on each spot
// 3. if you click on a ninja you must restart the game 
//    dojoDiv.innerHTML = `<button onclick="location.reload()">restart</button>`;

// start the game
// message to greet a user of the game
var style = "color:cyan;font-size:1.5rem;font-weight:bold;";
console.log("%c" + "IF YOU ARE A DOJO STUDENT...", style);
console.log("%c" + "GOOD LUCK THIS IS A CHALLENGE!", style);
// shows the dojo for debugging purposes
console.table(theDojo);
// adds the rows of buttons into <div id="the-dojo"></div> 
dojoDiv.innerHTML = render(theDojo);

