var btns = document.querySelectorAll("button");
var tom1 = new Audio("sounds/tom-1.mp3");




function makesound(key){
    var sound = new Audio("sounds/"+key+".mp3");
    sound.play();
}


/play sound on click/

    document.addEventListener("keydown", function(event){
    var key =event.key;
    buttunAnimation(key);
    makesound(key);
    console.log(key);        
        
    });


function buttunAnimation(key){
    document.querySelector("." + key).classList.toggle("pressed");
    setTimeout(() => {
        document.querySelector("." + key).classList.toggle("pressed");
    }, 100);
}
