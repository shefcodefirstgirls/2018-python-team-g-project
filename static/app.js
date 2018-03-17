
// var your.mapbox.access.token = "pk.eyJ1Ijoia2F0a29sZXIiLCJhIjoiY2pldm5xNnp1MGttZTMzbG5tbmV5M2gydyJ9.T1b6Ctnp5dA6gLfSsNb8Ow"

var mymap = L.map('mapid').setView([51.505, -0.09], 13);

L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}', {
    attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://mapbox.com">Mapbox</a>',
    maxZoom: 18,
    id: 'mapbox.streets',
    accessToken: "pk.eyJ1Ijoia2F0a29sZXIiLCJhIjoiY2pldm5xNnp1MGttZTMzbG5tbmV5M2gydyJ9.T1b6Ctnp5dA6gLfSsNb8Ow"
}).addTo(mymap);

var marker = L.marker([51.5, -0.09]).addTo(mymap);

var circle = L.circle([51.508, -0.11], {
    color: 'red',
    fillColor: '#f03',
    fillOpacity: 0.5,
    radius: 500
}).addTo(mymap);