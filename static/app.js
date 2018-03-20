
// var your.mapbox.access.token = "pk.eyJ1Ijoia2F0a29sZXIiLCJhIjoiY2pldm5xNnp1MGttZTMzbG5tbmV5M2gydyJ9.T1b6Ctnp5dA6gLfSsNb8Ow"

// import { GeoSearchControl, OpenStreetMapProvider } from 'leaflet-geosearch';

// const provider = new OpenStreetMapProvider();

// const searchControl = new GeoSearchControl({
//   provider: provider,
// });

var mymap = L.map('mapid').setView([0, 0], 1);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    minZoom: 1,
    id: 'mapbox.streets',
    accessToken: "pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw"
}).addTo(mymap);

// mymap.addControl(searchControl);

// var marker = L.marker([51.5, -0.09]).addTo(mymap);

// var circle = L.circle([51.508, -0.11], {
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.5,
//     radius: 500
// }).addTo(mymap);


// https://asmaloney.com/2015/06/code/clustering-markers-on-leaflet-maps/

$.getJSON( "hashtags", function( data ) {
	var markers = data.markers
	var markerClusters = L.markerClusterGroup();

	for ( var i = 0; i < markers.length; ++i )
	{
	  var popup = markers[i].screen_name +
	              '<br/>' + markers[i].location +
	              '<br/><b>Altitude:</b> ' + markers[i].text +
	              '<br/><b>Timezone:</b> ' + markers[i].time_zone;

	  var m = L.marker( [markers[i].lat, markers[i].lng])
	                  .bindPopup( popup );

	  markerClusters.addLayer( m );
	}

	mymap.addLayer( markerClusters );
});


// var markerClusters = L.markerClusterGroup();

// for ( var i = 0; i < markers.length; ++i )
// {
//   var popup = markers[i].screen_name +
//               '<br/>' + markers[i].location +
//               '<br/><b>Altitude:</b> ' + markers[i].text +
//               '<br/><b>Timezone:</b> ' + markers[i].time_zone;

//   var m = L.marker( [markers[i].lat, markers[i].lng])
//                   .bindPopup( popup );

//   markerClusters.addLayer( m );
// }

// mymap.addLayer( markerClusters );

// var marker = L.marker([-41.5, 10.09]).addTo(mymap);



