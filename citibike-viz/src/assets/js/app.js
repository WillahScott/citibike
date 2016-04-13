$(document).foundation();


L.mapbox.accessToken = 'pk.eyJ1Ijoid2lsbGFoc2NvdHQiLCJhIjoiY2lteWMwbm5uMDN6bHdibHV2OTlra2JzcSJ9.8vfJyRaTyZOYmsu2VTMTvA';
var map = L.mapbox.map('maptainer', 'mapbox.light')
    .setView([40.72, -73.99], 13);

var markNYC = L.marker([40.72, -73.99], {
	title:'Welcome to NYC!',
	clickable: true,
	opacity: .5,
});

markNYC.on('mouseover', function(e) {e.setOpacity(1);})
markNYC.on('mouseout', function(e) {e.setOpacity(.5);})
markNYC.on('click', function(e) {alert(e.getLatLng());})

markNYC.addTo(map);



