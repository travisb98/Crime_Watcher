var meter_needle =  document.querySelector("#meter_needle");
 
function range_change_event(danger_score) {
    var percent = danger_score*10;

    meter_needle.style.transform = "rotate(" + 
        (270 + ((percent * 180) / 100)) + "deg)";
    lbl.textContent = (danger_score);
}

// range_change_event(9);
