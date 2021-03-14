





var myMap = addMap(44.9778,-93.2650,api_key);


//// function that sends latitude and longitude to server in this format {'userlat':latitude, 'userlon':longitude}
function postToFlask(data){
    console.log('the data that will to flask is:')
    console.log(data);

    /// ideally I wouldn't want to hard code this url and other  variables. We'll need to make this dynamic so it works with python anywhere
    // var server_path = 'http://127.0.0.1:5000';
    var server_path = window.location.href;

    var post_path ='load';
    var url = server_path+post_path;

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        dataType: 'json'
    }).fail(function(xhr, status, error){
        console.log('error when posting to server')
        console.log(error);
        console.log(status);
        console.log(xhr);
        alert(error);
        console.log('post failed')
    }).done(function(data){
        console.log('response data received from server');
        console.log(data);

       ///// pan to user's location
        myMap.panTo(new L.LatLng(data.userData.userLat,data.userData.userLong));
        //// zoom in to user's location
        // myMap.setZoom(18);

        ///// add marker for user data
        addMarker(myMap,data.userData.userLat,data.userData.userLong,'green','Your Location');

        //// add markers for crime data
        for (var z =0; z < data.crimeData.length; z++){
            var message = `${data.crimeData[z].description}<br>${data.crimeData[z].time}<br>${data.crimeData[z].date} `
            addMarker(myMap,data.crimeData[z].centerLat,data.crimeData[z].centerLong,'red',message);

        };

        
    });
    
};


///// fucntion that is ran when the getCurrentPosition function is sucessful
function locationSucess(position){
    //// getting coordinates from the postition
    var user_coordinates = {'userLat':position.coords.latitude, 'userLong':position.coords.longitude};
    ///// posts the coordinates to the server
    postToFlask(user_coordinates);

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
function clickFunc(){
    ///// if the geolocation is true
    if(navigator.geolocation){
        var options = {timeout:60000,enableHighAccuracy: true};
        navigator.geolocation.getCurrentPosition(locationSucess,errorHandler,options);
    }
    else {
        alert('Geolocation is not supported by this browser.')
    };
};

// event listener
d3.selectAll('#button').on('click',clickFunc);
