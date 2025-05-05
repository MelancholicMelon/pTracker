// static/js/map_Ex.js
var map = L.map('map').setView([0, 0], 2);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

var userMarker, destinationMarker, routePolyline;

function setDestination(lat, lon) {
    var commonIcon = L.icon({
        iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
        shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
        iconSize: [25, 41],
        iconAnchor: [12, 41],
        popupAnchor: [1, -34],
        shadowSize: [41, 41]
    });

    if (destinationMarker) {
        destinationMarker.setLatLng([lat, lon]);
    } else {
        destinationMarker = L.marker([lat, lon], {icon: commonIcon}).addTo(map)
            .bindPopup('Destination')
            .openPopup();
    }

    map.destination = { lat: lat, lon: lon };

    if (routePolyline) {
        map.removeLayer(routePolyline);
    }
}
