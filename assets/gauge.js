/* Set radius for all circles */
var r = 250;
// var circles = document.querySelectorAll('.circle');
// var total_circles = circles.length;
// for (var i = 0; i < total_circles; i++) {
//     circles[i].setAttribute('r', r);
// }
 
/* Set meter's wrapper dimension */
var meter_dimension = (r * 2) + 100;
// var wrapper = document.querySelector("#wrapper");
// wrapper.style.width = meter_dimension + "px";
// wrapper.style.height = meter_dimension + "px";
 
/* Add strokes to circles  */
var cf = 2 * Math.PI * r;
var semi_cf = cf / 2;
// var semi_cf_1by4 = semi_cf / 4;
// var semi_cf_2by4 = semi_cf_1by4 * 2;
// var semi_cf_3by4 = semi_cf_1by4 * 3
// document.querySelector("#outline_curves")
//     .setAttribute("stroke-dasharray", semi_cf + "," + cf);
// document.querySelector("#low")
//     .setAttribute("stroke-dasharray", semi_cf + "," + cf);
// document.querySelector("#low-med")
//     .setAttribute("stroke-dasharray", semi_cf_2by3 + "," + cf);
// document.querySelector("#med-high")
//     .setAttribute("stroke-dasharray", semi_cf_1by3 + "," + cf);
// document.querySelector("#high")
//     .setAttribute("stroke-dasharray", semi_cf_1by3 + "," + cf);
// document.querySelector("#outline_ends")
//     .setAttribute("stroke-dasharray", 2 + "," + (semi_cf - 2));
// document.querySelector("#mask")
//     .setAttribute("stroke-dasharray", semi_cf + "," + cf);
 
// /* Bind range slider event*/
var lbl = document.querySelector("#lbl");
var mask = document.querySelector("#mask");
var meter_needle =  document.querySelector("#meter_needle");
 
function range_change_event() {
    var percent = 50;
    // var meter_value = semi_cf - ((percent * semi_cf) / 100);
    // mask.setAttribute("stroke-dasharray", meter_value + "," + cf);
    meter_needle.style.transform = "rotate(" + 
        (270 + ((percent * 180) / 100)) + "deg)";
    lbl.textContent = (percent/10);
}

range_change_event();
