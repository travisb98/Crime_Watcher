
///// fucntion that is ran when the getCurrentPosition function is sucessful
function locationSucess(position){
    //// getting lat and lon from the position
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;


    /////////// just printing out the results for now
    console.log('---------------');
    console.log('---------------');
    console.log('Position:');
    console.log(position);
    console.log('---------------');
    console.log('Coordinates');
    console.log(`Latitude:${latitude} ---Longitude: ${longitude}`);
    alert(`Latitude:${latitude} ---Longitude: ${longitude}`);
    console.log('---------------');
    console.log('---------------');

};

/// error handler that is ran when getCurrentPosition is NOT sucessful
function errorHandler(err) {
    if(err.code == 1) {
        alert("Error: Access is denied!");
    } else if( err.code == 2) {
        alert("Error: Position is unavailable!");
    }
};
///// main function that will be passed to event handler
function getLocation(){
    ///// if the geolocation
    if(navigator.geolocation){
        var options = {timeout:60000,enableHighAccuracy: true};
        navigator.geolocation.getCurrentPosition(locationSucess,errorHandler,options);
    }
    else {
        alert('Geolocation is not supported by this browser.')
    };

};


//////////// event listener for button click that runs the getLocation function.
////// we could do  something else with this button, but we'll just use it to console log coordinates for now
d3.selectAll('#button').on('click',getLocation);

///////// psuedo code for potential event listener:
// d3.selectAll('#button').on('click',getLocation).then(//// some sort of function that sends the location variables to the flask server)



//// everything below this obnoxious block is test code
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////
////////////////////////////////////////////////////////////////////////////////////////////////////





// //// event handler for the change of permission status.. this hasn't been working form me
// PermissionStatus.onchange = function(){
//     console.log("permission status changed");
//     alert("permission status changed")
// };

// PermissionStatus.addEventListener('change',function(){console.log("permission status changed")});


/////// implicitly passing query results to console log

// navigator.permissions.query({ name: 'geolocation' }).then(console.log)


///// 
// navigator.permissions.query({ name: 'geolocation' }).state.then(console.log)

// while()

