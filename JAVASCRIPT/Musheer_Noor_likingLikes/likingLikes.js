
    var numOfLikes1 = 3;
    var numOfLikes2 = 3;
    var numOfLikes3 = 3;

function increaseLikes(element){
    var bttn = element.id;
    console.log(bttn);

        if (bttn === "likeButton1"){
            numOfLikes1 = numOfLikes1 + 1;
            document.getElementById("toph4").innerText = numOfLikes1 + " likes(s)";
        }
        else if (bttn === "likeButton2"){
            numOfLikes2 = numOfLikes2 + 1;
            document.getElementById("midh4").innerText = numOfLikes2 + " likes(s)";
        }
        else if (bttn === "likeButton3"){
            numOfLikes3 = numOfLikes3 + 1;
            document.getElementById("bttmh4").innerText = numOfLikes3 + " likes(s)";
        }
}

