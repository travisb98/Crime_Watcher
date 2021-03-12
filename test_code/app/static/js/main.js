

function loadPage(){
    /////// BOOO  this shouldn't be hard coded
    var server_path = 'http://127.0.0.1:5000/';
    // var post_path ='';
    var post_path ='results';
    ///// just opening the coor path, essentially trying to send a get request to the coor route
    window.location.href = server_path+post_path;
};


//// function that sends latitude and longitude to server in this format {'userlat':latitude, 'userlon':longitude}
function postToFlask(data){

    /// ideally I wouldn't want to hard code this url and other  variables. We'll need to make this dynamic so it works with python anywhere
    var server_path = 'http://127.0.0.1:5000/';
    // var post_path ='';
    var post_path ='coor';
    var url = server_path+post_path;
    var dataType = 'json';

    
    // $.ajax({
    //     type: "POST",
    //     url: url,
    //     data: data,
    //     success: function(){console.log("success function ran")},
    //     dataType: dataType
    // });

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        dataType: dataType
    }).fail(function(){

        ///// this is bad but it works, JAVASCRIPT says this post is failing to load but it isn't  
        loadPage();
        console.log('post failed')
    });

};



////do PULLS or GETS to the server via ajax
function AJAXToFlask(data,typePG){

    /// ideally I wouldn't want to hard code this url and other  variables. We'll need to make this dynamic so it works with python anywhere
    var server_path = 'http://127.0.0.1:5000/';
    // var post_path ='results';
    var post_path ='coor';
    var url = server_path+post_path;
    var dataType = 'json';


    $.ajax({
        type: typePG,
        url: url,
        data: data,
        dataType:dataType,

    }).done(function(msg){
        console.log(`ajax request complete with message: ${msg}`);
        // loadPage();
        

    }).fail(function(){console.log('request failed')});



};


///// fucntion that is ran when the getCurrentPosition function is sucessful
function locationSucess(position){

    //// getting lat and lon from the position
    var latitude = position.coords.latitude;
    var longitude = position.coords.longitude;
    var coordinates = {'userlat':latitude, 'userlon':longitude};

    /////// function from map.js
    // mapCoordinates(coordinates);

    ///// posts the coordinates to the server
    postToFlask(coordinates);

    ///// posts the coordinates to the server
    // AJAXToFlask(coordinates,'POST');



    // pauseFunc;

    
    // /////// function from map.js
    // mapCoordinates(coordinates);


    /////////// just printing out the results for now
    console.log('---------------');
    console.log('Coordinates in Location Success Function');
    console.log(`Latitude:${latitude} ---Longitude: ${longitude}`);
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



// function loadPage(){
//     /////// BOOO  this shouldn't be hard coded
//     var server_path = 'http://127.0.0.1:5000/';
//     // var post_path ='';
//     var post_path ='coor';
//     ///// just opening the coor path, essentially trying to send a get request to the coor route
//     window.location.href = server_path+post_path;
// };



///// to set a delay
function pauseFunc(){

    setTimeout(function(){
        alert("I am setTimeout");
    },1000); //delay is in milliseconds 

};




function clickFunc(){

    ///// run get location function to sent POST request to server
    
    ////// time delay
    ////// load new page
    // $.when(getLocation).then(pauseFunc).then(loadPage);
    // $.when(getLocation).then(loadPage);
    // getLocation;
    // loadPage;


};

//// event handler for button
// d3.selectAll('#button').on('click',clickFunc);

d3.selectAll('#button').on('click',getLocation);






// psuedo code
//  on button click, post results to server, THEN load new page, THEN add map to results page





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

// ////do PULLS or GETS to the server via ajax
// function AJAXToFlask(data,typePG){

//     /// ideally I wouldn't want to hard code this url and other  variables. We'll need to make this dynamic so it works with python anywhere
//     var server_path = 'http://127.0.0.1:5000/';
//     // var post_path ='results';
//     var post_path ='coor';
//     var url = server_path+post_path;
//     var dataType = 'json';

//     $.ajax({
//         type: typePG,
//         url: url,
//         data: data,
//         success: function(){console.log("success function ran")},
//         dataType: dataType
//     });
// };













// ///////// potentially useful time delay code
// alert("before setTimeout");

// setTimeout(function(){
//         alert("I am setTimeout");
//    },1000); //delay is in milliseconds 

//   alert("after setTimeout");
// // ////////////////////////




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

