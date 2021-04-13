

function processUserData(data, myMap) {
    var userLat = data.userData.userLat;
    var userLong = data.userData.userLong;
    var dangerScore = data.userData.dangerScore;
    ///// pan to user's location
    myMap.panTo(new L.LatLng(userLat, userLong))

    ///// gauge function
    range_change_event(dangerScore);

    //// zoom in to user's location
    myMap.setView([parseFloat(userLat), parseFloat(userLong)], 14);

    

    // get the selected location so we can add it to the marker
    var markerText = $('#SelectedLocation option:selected').text();

    ///// add marker for user data
    addMarker(myMap, userLat, userLong, 'green', markerText);
    ////// post their danger score 
    $('#gaugeLabel').html(`Your danger score is ${dangerScore}`);
    ////// add label to map
    // $('#mapLabel').html(`Your coordinates are ${userLat},${userLong}`);
};

// process each nearby crime 
function processCrimeData(data, myMap) {

    var dataSet = [];

    // if the api returns 0 results for nearby crimes
    if (data.crimeData === undefined || data.crimeData.length == 0) {

        //// label list
        $('#listLabel').html('Congratulations, there are no recent crimes in your area.');

    }
    // if any crimes were returned from the api .... 
    else {
        // for each of the crimes in the list of crimes
        data.crimeData.forEach(function (crime) {
            var date = crime.date;
            var time = crime.time;
            var centerLat = crime.centerLat;
            var centerLong = crime.centerLong;
            var description = crime.description;
            var address = crime.address;
            // add markers for crime data
            var markerText = `${description}<br>${time}<br>${date} `
            addMarker(myMap, centerLat, centerLong, 'red', markerText);
            // label list
            // $('#listLabel').html('Crimes in your area:')

            // add the description time and date to the list
            // $('#list').append(`<li>${description}</li>
            // <ul><li>${time}</li><li>${date}</li><li>${address}</li><ul>`)

            dataSet.push([date, time, description, address.split(",").splice(0, 3).join()])
        });

        $('table').DataTable({
            data: dataSet,
            columns: [
                { title: "Date" },
                { title: "Time" },
                { title: "Description" },
                { title: "Address" }
            ]
        });

        
    };

    $("#loading").hide()
    $("#map").css("z-index", "");
};

// function to handle errors when posting data to server
function postErrorHandler(xhr, status, error) {
    console.log('error when posting to server')
    console.log(`POST Error: ${error}`);
    console.log(`Status: ${status}`);
    console.log(`XHR: ${xhr}`);
    alert(`POST Error ${error}`)
}

// function that sends latitude and longitude to server in this format {'userlat':latitude, 'userlon':longitude}
function postToFlask(data) {
    console.log('the data that will be sent to flask is:')
    console.log(data);

    //get the base path and the loading route
    var server_path = window.location.href;
    var post_path = 'load';
    var url = server_path + post_path;

    $.ajax({
        type: "POST",
        url: url,
        data: data,
        dataType: 'json'
    }).fail(function (xhr, status, error) {
        // function to handle errors with posting
        postErrorHandler(xhr, status, error);
    }).done(function (data) {
        console.log('response data received from server:');
        console.log(data);

        // deleteMarkers(myMap);
        //  process the crime data
        processCrimeData(data, myMap);
        // process the user's data
        processUserData(data, myMap);
    });

};


// fucntion that is ran when the getCurrentPosition function is sucessful
function locationSucess(position) {

    // getting coordinates from the postition
    var user_coordinates = {'userLat':position.coords.latitude, 'userLong':position.coords.longitude};

    $("#map").css("z-index", "-1");
    $("#loading").show()
    // posts the coordinates to the server
    postToFlask(user_coordinates);

};

// error handler that is ran when getCurrentPosition is NOT sucessful
function errorHandler(err) {
    if (err.code == 1) {
        alert("Error: Access is denied!");
    } else if (err.code == 2) {
        alert("Error: Position is unavailable!");
    }
};

///// fucntion that is ran when using the dropdown options
function locationDropdown(lat,long) {
    var user_coordinates = { 'userLat': lat, 'userLong': long };

    $("#map").css("z-index", "-1");
    $("#loading").show()
    ///// posts the coordinates to the server
    postToFlask(user_coordinates);

};

//  function that will be passed to event handler
function clickFunc() {

    var dropDown = document.getElementById("SelectedLocation");
    var dropDownText = dropDown.options[dropDown.selectedIndex].text;

    if (dropDownText == "My Location") {
        // This handler is making sure that we have access to the user's geolocation when they select "My Location"
        if (navigator.geolocation) {
            var options = { timeout: 60000, enableHighAccuracy: true };
            navigator.geolocation.getCurrentPosition(locationSucess, errorHandler, options);
        }
        else {
            alert('Geolocation is not supported by this browser.')
        };
    }
    else {
        // This uses the coordinates for the selected dropdown location
        var latlongStr=dropDown.value.slice(1,length-1).split(",");
        var lat= parseFloat(latlongStr[0]);
        var long= parseFloat(latlongStr[1].trim());
        locationDropdown(lat,long);
    };


};

// event listener
d3.selectAll('#button').on('click', clickFunc);
