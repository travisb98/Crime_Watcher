


//// function that sends latitude and longitude to server in this format {'userlat':latitude, 'userlon':longitude}
function postToFlask(data){

    /// ideally I wouldn't want to hard code this url. We'll need to make this dynamic so it works with python anywhere
    var server_path = 'http://127.0.0.1:5000/';

    var post_path ='coor';

    var url = server_path+post_path;

    var dataType = 'json';

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        success: function(){console.log("success function ran")},
        dataType: dataType
    });
};


///// fucntion that is ran when the getCurrentPosition function is sucessful
function locationSucess(position){

    //// getting lat and lon from the position
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;

    var coordinates = {'userlat':latitude, 'userlon':longitude};

    ///// posts the coordinates to the server
    postToFlask(coordinates);

    /////////// just printing out the results for now
    console.log('---------------');
    console.log('---------------');
    console.log('Position:');
    console.log(position);
    console.log('---------------');
    console.log('Coordinates');
    console.log(`Latitude:${latitude} ---Longitude: ${longitude}`);
    // alert(`Latitude:${latitude} ---Longitude: ${longitude}`);
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
    ///// if the geolocation is true
    if(navigator.geolocation){
        var options = {timeout:60000,enableHighAccuracy: true};
        navigator.geolocation.getCurrentPosition(locationSucess,errorHandler,options);
    }
    else {
        alert('Geolocation is not supported by this browser.')
    };

};

//// event handler for button
d3.selectAll('#button').on('click',getLocation);



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






// function extractCoordinates(){
//     ///// if the geolocation is true
//     if(navigator.geolocation){
//         var options = {timeout:60000,enableHighAccuracy: true};

//         navigator.geolocation.getCurrentPosition(function extractSuccess(position){
//             var latitude = position.coords.latitude;
//             var longitude = position.coords.longitude;

//             return {'userlat':latitude, 'userlon':longitude}




//             },errorHandler,options)
//     }
//     else {
//         alert('Geolocation is not supported by this browser.')
//     };

//     return {'userlat':latitude, 'userlon':longitude}



// };

// extractCoordinates();

//////////// event listener for button click that runs the getLocation function.
////// we could do  something else with this button, but we'll just use it to console log coordinates for now
// d3.selectAll('#button').on('click',getLocation);

// d3.selectAll('#button').on('click',getLocation);
// getLocation();


// console.log(`extracted lat: ${latitude}--extracted lat: ${longitude}`);

// getLocation().then(console.log(`extracted lat: ${lat}--extracted lat: ${lon}`));
// console.log(`extracted lat: ${lat}--extracted lat: ${lon}`);




///////// psuedo code for potential event listener:
// d3.selectAll('#button').on('click',getLocation).then(//// some sort of function that sends the location variables to the flask server)
// getLocation();




////// just setting this as random coordinates for now, we'll want to use the getLocation fucntion to actually grab these coordinates
// var coordinates = {'userlat':42.01, 'userlon':69.69};


// /// ideally I wouldn't want to hard code this url ideally it would be 
// var server_path = 'http://127.0.0.1:5000/';

// var post_path ='coor';

// var url = server_path+post_path;

// var dataType = 'json';
// function success(){console.log("success function ran")};

// $.ajax({
//     type: "POST",
//     url: url,
//     data: coordinates,
//     success: success,
//     dataType: dataType
//   });




// function postToFlask(data){

//     /// ideally I wouldn't want to hard code this url ideally it would be 
//     var server_path = 'http://127.0.0.1:5000/';

//     var post_path ='coor';

//     var url = server_path+post_path;

//     var dataType = 'json';

//     $.ajax({
//         type: "POST",
//         url: url,
//         data: data,
//         success: function(){console.log("success function ran")},
//         dataType: dataType
//     });
// };







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

