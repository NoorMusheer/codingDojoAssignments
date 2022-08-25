function getSecondsSinceStartOfDay() {
    return new Date().getSeconds() +
        new Date().getMinutes() * 60 +
        new Date().getHours() * 3600;
}

setInterval(function () {
    var crntHr = new Date().getHours();
    var crntMin = new Date().getMinutes();
    var crntSec = new Date().getSeconds();

    document.querySelector("#currentHour").innerText = (((crntHr/12)-1)*12) + ":";

    document.querySelector("#currentMinute").innerText = crntMin + ":";
    
    document.querySelector("#currentSeconds").innerText = crntSec;

    document.querySelector("#hour").style.transform = "rotate(" + ((crntHr*30)+(crntMin*.5)+(crntSec *((360)/(43200)))+180) + "deg)"

    document.querySelector("#minutes").style.transform = "rotate(" + (((new Date().getMinutes())*6)+((new Date().getSeconds())*.1)+180)+ "deg)"

    document.querySelector("#seconds").style.transform = "rotate(" + (((new Date().getSeconds())*6)+180) + "deg)"
}, 1000);

