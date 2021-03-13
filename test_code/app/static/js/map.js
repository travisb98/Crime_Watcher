



function mapCoordinates(usercoordinates,crimecoordinates,crime_descriptions){
  // console.log(`coordinates preformant in map function :${usercoordinates}`);
  // console.log('-----------');
  // console.log('-----------');
  // console.log(usercoordinates[0]);
  // console.log(typeof(usercoordinates[0]));
  // console.log('-----------');
  // console.log('-----------');


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
  marker.bindPopup("your location");

  ///// download red marker from site
  var redIcon = new L.Icon({
    iconUrl: 'https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-red.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
    iconSize: [25, 41],
    iconAnchor: [12, 41],
    popupAnchor: [1, -34],
    shadowSize: [41, 41]
  });

  /////////// adding the crime markers
  for (var z =0; z < Object.keys(crimecoordinates).length; z++){
    var currentcoor = crimecoordinates[z];
    //// make marker for each crime, make the icon red, and bind the description as a pop-up
    L.marker(currentcoor, {title: "marker",icon:redIcon}).addTo(myMap).bindPopup(crime_descriptions[z]);
  };

};






