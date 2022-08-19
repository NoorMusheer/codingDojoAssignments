

function delDonateBtn(element){
    element.remove();
}

function typeChosen(petType){
        alert("You are looking for a " + petType.value)
}


var likes =[3,5,8]
var petTags = [
    document.querySelector("#peppersPettings"),
    document.querySelector("#brucesPettings"),
    document.querySelector("#oscarsPettings")
]
function increasePetting(pet){
    likes[pet]++;
    petTags[pet].innerText = likes[pet] + " petting(s)";
}