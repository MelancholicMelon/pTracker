// static/js/locate.js
function locateUser() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var userLat = position.coords.latitude;
                var userLon = position.coords.longitude;

                map.setView([userLat, userLon], 12);

                var commonIcon = L.icon({
                    iconUrl: 'https://cdn-icons-png.flaticon.com/512/7509/7509047.png',
                    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
                    iconSize: [25, 30],
                    iconAnchor: [12, 41],
                    popupAnchor: [1, -34],
                    shadowSize: [41, 41]
                });

                if (userMarker) {
                    userMarker.setLatLng([userLat, userLon]);
                } else {
                    userMarker = L.marker([userLat, userLon], {icon: commonIcon}).addTo(map)
                        .bindPopup('You are here!')
                        .openPopup();
                }
            },
            function(error) {
                switch(error.code) {
                    case error.PERMISSION_DENIED:
                        alert("User denied the request for Geolocation.");
                        break;
                    case error.POSITION_UNAVAILABLE:
                        alert("Location information is unavailable.");
                        break;
                    case error.TIMEOUT:
                        alert("The request to get user location timed out.");
                        break;
                    case error.UNKNOWN_ERROR:
                        alert("An unknown error occurred.");
                        break;
                }
            },
            {timeout: 10000, enableHighAccuracy: true, maximumAge: 0}
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
