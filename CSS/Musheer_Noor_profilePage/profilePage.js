

console.log("hello");

var userName = document.querySelector("#profile-card-main h1");
console.log(userName);

function changeName(){
    userName.innerText = "Madi"
    
};
var userRequest = document.querySelector(".requestsForConnection1")
function removeRequest(){
    userRequest.remove();
}


var userRequest2 = document.querySelector(".requestsForConnection2")
function removeRequest2(){
    userRequest2.remove();

}