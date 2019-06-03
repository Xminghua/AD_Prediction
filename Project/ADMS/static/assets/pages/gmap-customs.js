$( document ).ready(function() {
	// Simple map
    function initialize() {
        var mapOptions = {
            center: new google.maps.LatLng(40.741895,-73.989308),
            zoom: 9
        };
        var map = new google.maps.Map(document.getElementById('map'),  mapOptions); 
    }
    google.maps.event.addDomListener(window, 'load', initialize);
    
});