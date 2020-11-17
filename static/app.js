// var your.mapbox.access.token = "pk.eyJ1Ijoia2F0a29sZXIiLCJhIjoiY2pldm5xNnp1MGttZTMzbG5tbmV5M2gydyJ9.T1b6Ctnp5dA6gLfSsNb8Ow"

var mymap = L.map('mapid').setView([0, 0], 1);

L.tileLayer('https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    minZoom: 1,
    id: 'mapbox/streets-v11',
    accessToken: "pk.eyJ1Ijoia2F0a29sZXIiLCJhIjoiY2pldm5xNnp1MGttZTMzbG5tbmV5M2gydyJ9.T1b6Ctnp5dA6gLfSsNb8Ow", 
    subdomains: ['a','b','c']
}).addTo(mymap);

var myIcon = L.icon({
  iconUrl: '/static/pin24.png',
  iconRetinaUrl: '/static/pin48.png',
  iconSize: [29, 24],
  iconAnchor: [9, 21],
  popupAnchor: [0, -14]
});

// var circle = L.circle([51.508, -0.11], {
//     color: 'red',
//     fillColor: '#f03',
//     fillOpacity: 0.5,
//     radius: 500
// }).addTo(mymap);

// https://asmaloney.com/2015/06/code/clustering-markers-on-leaflet-maps/

var query = encodeURIComponent(query)
var search_url = "hashtags/" + query + "/" + numbertweets ;

// console.log(search_url);
document.getElementById("loading").style.display = "inline";

$.getJSON( search_url, function( data ) {
	var markers = data.markers
	var markerClusters = L.markerClusterGroup({
		spiderfyOnMaxZoom: true,
		showCoverageOnHover: true,
		zoomToBoundsOnClick: true
	});

	for ( var i = 0; i < markers.length; ++i )
	{
	  var popup = '<br/><b>User:</b><a href=\"https://twitter.com/' + markers[i].screen_name + '\" target=\"_blank\">' + markers[i].screen_name + '</a>' +
	  				'<br/><b>Created at:</b> ' + markers[i].created_at +
	  	          '<br/><b>Tweet:</b> ' + markers[i].text +
	  	          '<br/><b>Tweet Link:</b><a href=\"https://twitter.com/i/web/status/' + markers[i].id_str + '\" target=\"_blank\">' + markers[i].id_str + '</a>' +
	              '<br/><b>Location:</b> ' + markers[i].location +
	              '<br/><b>Timezone:</b> ' + markers[i].time_zone;

	  var m = L.marker( [markers[i].lat, markers[i].lng], {icon: myIcon} ).bindPopup( popup );

	  markerClusters.addLayer( m );
	}
	document.getElementById("loading").style.display = "none";
	mymap.addLayer( markerClusters );
});
