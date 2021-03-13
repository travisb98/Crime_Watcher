// var myMap = L.map("map", {
//   center: coordinates,
//   zoom: 13
// });



function mapCoordinates(usercoordinates,crimecoordinates){
  console.log(`coordinates preformant in map function :${usercoordinates}`)

  // unpacking coordinates for leafly format
  // coordinates = [coordinates['userlat'],coordinates['userlon']]
  // console.log(`coordinates postformant in map function :${coordinates}`)

  // Create our initial map object
  // Set the longitude, latitude, and the starting zoom level
  var myMap = L.map("map", {
    center: usercoordinates,
    zoom: 13
  });

  // Add a tile layer (the background map image) to our map
  // We use the addTo method to add objects to our map
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom: 18,
    zoomOffset: -1,
    id: "mapbox/streets-v11",
    accessToken: api_key
  }).addTo(myMap);

  // Create a new marker
  // Pass in some initial options, and then add it to the map using the addTo method
  var marker = L.marker(usercoordinates, {
    title: "marker"
  }).addTo(myMap);

  // Binding a pop-up to our marker
  marker.bindPopup("Hello There!");

  console.log(' crime coordinate type');
  console.log(typeof(crimecoordinates));

  console.log('all crime coordinates');
  console.log(crimecoordinates);

  console.log('first crime coordinate');
  console.log(crimecoordinates[27]);



  // /////////// adding the crime markers
  // for (var z =0; z < crimecoordinates.length;z++){

  //   console.log(crimecoordinates[z]);

  //   // var marker = L.marker(usercoordinates[z], {
  //   //   title: "marker"
  //   // }).addTo(myMap);
  //   // // Binding a pop-up to our marker
  //   // marker.bindPopup("Hello There!");

  // };


};


// var myMap = L.map("map", {
//   center: [-93.01,44.01],
//   zoom: 13
// });


// // Add a tile layer (the background map image) to our map
// // We use the addTo method to add objects to our map
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: api_key
// }).addTo(myMap);


// function addMarkerAndPopup(coordinates,message){
//   // Create a new marker
//   // Pass in some initial options, and then add it to the map using the addTo method
//   var marker = L.marker(coordinates, {
//     title: "marker"
//   }).addTo(myMap);

//   // Binding a pop-up to our marker
//   marker.bindPopup(message);

// };




// testcoord = {'userlat':45.27, 'userlon':-93.27}
// mapCoordinates(testcoord);

// user_coordinates = {'userlat':45.27, 'userlon':-93.27};
// Create our initial map object
// Set the longitude, latitude, and the starting zoom level



  // console.log(`coordinates preformant in map function :${user_coordinates}`);

  // // unpacking coordinates for leafly format
  // coordinates = [user_coordinates['userlat'],user_coordinates['userlon']];

  // console.log(`coordinates postformant in map function :${user_coordinates}`);

// user_coordinates = [45.27,-93.27]


// var myMap = L.map("map", {
//   center: user_coordinates,
//   zoom: 13
// });

// // Add a tile layer (the background map image) to our map
// // We use the addTo method to add objects to our map
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: api_key
// }).addTo(myMap);

// // Create a new marker
// // Pass in some initial options, and then add it to the map using the addTo method
// var marker = L.marker(user_coordinates, {
//   title: "marker"
// }).addTo(myMap);

// // Binding a pop-up to our marker
// marker.bindPopup("Hello There!");


/////////////////////////////////////////////////////////////////////////////////////////////////
/////////////////////////////////////
/////////////////////////////////////
/////////////////////////////////////

// var user_coordinates = [44.974832099355186,-93.27689766883852]

// // Create our initial map object
// // Set the longitude, latitude, and the starting zoom level
// var myMap = L.map("map", {
//   center: user_coordinates,
//   zoom: 13
// });

// // Add a tile layer (the background map image) to our map
// // We use the addTo method to add objects to our map
// L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
//   attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
//   tileSize: 512,
//   maxZoom: 18,
//   zoomOffset: -1,
//   id: "mapbox/streets-v11",
//   accessToken: api_key
// }).addTo(myMap);


// // Create a new marker
// // Pass in some initial options, and then add it to the map using the addTo method
// var marker = L.marker(user_coordinates, {
//   title: "marker"
// }).addTo(myMap);

// // Binding a pop-up to our marker
// marker.bindPopup("Hello There!");