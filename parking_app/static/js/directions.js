// static/js/directions.js
function getDirections(userLat, userLon, destLat, destLon, selectedMode) {
    const apiKey = 'SECRET';  // Replace with your OpenRouteService API key
    const url = `https://api.openrouteservice.org/v2/directions/${selectedMode}?api_key=${apiKey}&start=${userLon},${userLat}&end=${destLon},${destLat}`;
    console.log("Selected option",selectedMode)
    fetch(url)
        .then(response => response.json())
        .then(data => {
            var coordinates = data.features[0].geometry.coordinates;
            var latlngs = coordinates.map(coord => [coord[1], coord[0]]);

            if (routePolyline) {
                map.removeLayer(routePolyline);
            }

            routePolyline = L.polyline(latlngs, { color: 'blue' }).addTo(map);
            map.fitBounds(routePolyline.getBounds());
        })
        .catch(error => {
            console.error('Error fetching directions:', error);
        });
}

function navigateUser(selectedMode) {
    console.log("selectedMode ", selectedMode);
    radius = 3000
    if (userMarker && map.destination) {
        var userLat = userMarker.getLatLng().lat;
        var userLon = userMarker.getLatLng().lng;
        var destLat = map.destination.lat;
        var destLon = map.destination.lon;
        getDirections(userLat, userLon, destLat, destLon, selectedMode);
    } else {
        locateUser()
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(position => {
                var userLat = position.coords.latitude;
                var userLon = position.coords.longitude;
                
                var filtLot = [];
                fetch('/static/parking_app/data/ParkingDB_OSM.csv')
                    .then(response => response.text())
                    .then(data => {
                        const parkingLots = parseCSV(data);
                        
                        for (var i = 0; i < parkingLots.length; i++) {
                            var row = parkingLots[i];
                            var lat = parseFloat(row.Latitude);
                            var lon = parseFloat(row.Longitude);

                            var dLat = (lat - userLat) * (Math.PI / 180);
                            var dLon = (lon - userLon) * (Math.PI / 180);
                            var a = Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                                    Math.cos(userLat * (Math.PI / 180)) * Math.cos(lat * (Math.PI / 180)) *
                                    Math.sin(dLon / 2) * Math.sin(dLon / 2);
                            var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
                            var distance = 6371e3 * c; // Earth's radius in meters

                            if (distance <= radius) {
                                filtLot.push(parkingLots[i]);
                            }
                        }
                        
                        if (filtLot.length > 0) {
                            filtLot.sort((a, b) => parseFloat(a.Distance) - parseFloat(b.Distance));
                            let lat = parseFloat(filtLot[0].Latitude);
                            let lon = parseFloat(filtLot[0].Longitude);
                            displayParkingLots(filtLot, userLat, userLon);
                            getDirections(userLat, userLon, lat, lon, selectedMode);
                        } else {
                            console.log('No parking lots found within the specified radius.');
                        }
                    })
                    .catch(error => console.error('Error fetching parking lots data:', error));
            }, error => {
                console.error('Error getting user location:', error);
            });
        } else {
            console.error('Geolocation is not supported by this browser.');
        }
    }
}
