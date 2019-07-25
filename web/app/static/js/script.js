
        
// setTimeout(function() {
//     $("#button").hide();
// }, 2000);

// function playVid(timings) { 
//     console.log(timings);
//     vid.currentTime = 5; //put in the skip time here 
//     vid.play();
// }


$(document).ready(function() {

    
var vid = document.getElementById("video"); 

setInterval(updateUI, 500);


startTimes = [];
stopTimes = [];
currentSkipTime = 0;

processTimings();

function processTimings() {
    timings.forEach(obj => {
        startTimes.push(obj.start);
        stopTimes.push(obj.stop);
    });
}

function updateUI() {

    currentTime = vid.currentTime;

    console.log("update" + currentTime);

    startTimes.forEach(function(startTime, index) {
        if (Math.round(currentTime) == startTime) {
            currentSkipTime = stopTimes[index];
            showButton();
        }
    });

    stopTimes.forEach(function(stopTime, idx) {
        if (Math.round(currentTime) == stopTime) {
            hideButton();
        }
    });
}


function showButton() {
    $("#button").fadeIn();
    setTimeout(hideButton, 8500);
}

function hideButton() {
    $("#button").fadeOut();
}

$("#button").click(function() {
    vid.currentTime = currentSkipTime - 2;
});

});
