


function alwaysHungry(arr) {
    // your code here 
    var hasEaten = false; 
    for (i=0; i<arr.length; i++){
        if (arr[i] == "food"){
            console.log("yummy");
            hasEaten = true;
        }
    }
    if (hasEaten == false){
        console.log("i'm hungry");
    }

};

alwaysHungry([3.14, "food", "pie", true, "food"]);




// this should console log "yummy", "yummy"
alwaysHungry([4, 1, 5, 7, 2]);
// this should console log "I'm hungry"


