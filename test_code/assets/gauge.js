/* Set radius for all circles */
var r = 250;

 
/* Set meter's wrapper dimension */
var meter_dimension = (r * 2) + 100;

 
/* Add strokes to circles  */
var cf = 2 * Math.PI * r;
var semi_cf = cf / 2;
/// /* Bind range slider event*/
var lbl = document.querySelector("#lbl");
var mask = document.querySelector("#mask");
var meter_needle =  document.querySelector("#meter_needle");
 
function range_change_event(danger_score) {
    var percent = danger_score*10;

    meter_needle.style.transform = "rotate(" + 
        (270 + ((percent * 180) / 100)) + "deg)";
    lbl.textContent = (danger_score);
}

range_change_event(9);
