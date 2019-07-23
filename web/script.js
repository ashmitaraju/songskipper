var vid = document.getElementById("video"); 
        
setTimeout(function() {
    $("#button").hide();
}, 2000);

function playVid() { 
    vid.currentTime = 5; //put in the skip time here 
    vid.play();
}