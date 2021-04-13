
// console.log(api_key);

////// pass a lowercase string color(ie 'red') and it should return that color, I only tried it for red and green
///// maybe we could use a color scale to indicate the intensity of the crimes.........??????
function colorIcon(color){
    ///// download marker from site with the selected color
    var icon = new L.Icon({
      iconUrl: `https://raw.githubusercontent.com/pointhi/leaflet-color-markers/master/img/marker-icon-2x-${color}.png`,
      shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/0.7.7/images/marker-shadow.png',
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowSize: [41, 41]
    });
  return icon ;
};

//////// adds the map to the  
function addMap(lat,lon,api_key){
  var myMap = L.map("map", {
    center: [lat,lon],
    zoom: 12
  });

  // L.titleLayer.accessToken ='{{api_key}}';
  // Add background layer 
  ////// i wonder if we could make 
  L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    tileSize: 512,
    maxZoom:18,
    zoomOffset: -1,
    id: "mapbox/dark-v9",
    accessToken: api_key
  }).addTo(myMap);

  console.log('Title layer')


  return myMap




};


////// coordinates should be in [44.9778,-93.2650] format, color in 'red' format and text as a 'string'
function addMarker(myMap,lat,lon,color,text){
  L.marker([lat,lon], {title: "marker",icon:colorIcon(color)}).addTo(myMap).bindPopup(text);

};

