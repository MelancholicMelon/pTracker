let markerLayerGroup = L.layerGroup().addTo(map);

function findNearbyParkingLots(radius) {
    if(radius == 0){
        radius = 3000
    }
    console.log(radius, " is radius")
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var userLat = position.coords.latitude;
                var userLon = position.coords.longitude;
                fetchNearbyParkingLots(userLat, userLon,radius);
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

function fetchNearbyParkingLots(userLat, userLon, radius) {
    //var radius = 10000
    console.log("Showing parkings in a radius of ", radius)
    var filtLot = []
    fetch('/static/parking_app/data/ParkingDB_OSM.csv')
        .then(response => response.text())
        .then(data => {
            const parkingLots = parseCSV(data);
            for (var i = 0; i < parkingLots.length; i++) {
                //console.log("This does run");
                var row = parkingLots[i];
                var lat = parseFloat(row.Latitude);
                var lon = parseFloat(row.Longitude);
                //console.log("Lat n Lon",lat,lon)
                // Haversine formula to calculate the distance between two points on the Earth
                var dLat = (lat - userLat) * (Math.PI / 180);
                var dLon = (lon - userLon) * (Math.PI / 180);
                var a = 
                    Math.sin(dLat / 2) * Math.sin(dLat / 2) +
                    Math.cos(userLat * (Math.PI / 180)) * Math.cos(lat * (Math.PI / 180)) *
                    Math.sin(dLon / 2) * Math.sin(dLon / 2);
                var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
                var distance = 6371e3 * c; // Earth's radius in meters
                //console.log(distance)
        
                if (distance <= radius) {
                    console.log("Found!");
                    //console.log("Pushing ", parkingLots[i])
                    filtLot.push(parkingLots[i])
                }
                filtLot.sort()
                //console.log(filtLot)
            }
            displayParkingLots(filtLot, userLat, userLon);
            return filtLot
        })
        .catch(error => console.error('Error fetching parking lots data:', error));
}

function parseCSV(data) {
    const lines = data.split('\n');
    const result = [];
    const headers = lines[0].split(',');

    for (let i = 1; i < lines.length; i++) {
        const obj = {};
        const currentline = lines[i].split(',');

        for (let j = 0; j < headers.length; j++) {
            obj[headers[j].trim()] = currentline[j].trim();
        }
        result.push(obj);
    }
    return result;
}

function displayParkingLots(parkingLots, userLat, userLon) {
    markerLayerGroup.clearLayers();
    console.log('Displaying parking lots:', parkingLots);
    parkingLots.forEach(function(parkingLot) {
        let lat = parseFloat(parkingLot.Latitude);
        let lon = parseFloat(parkingLot.Longitude);
        let name = parkingLot.Name || "Parking Lot";
        let availability = parseInt(parkingLot.Current_Free_Spot, 10);
        let car = parkingLot.Car;
        let bike = parkingLot.Bicycle;
        let motor = parkingLot.Motorcycle;
        let gentsuki = parkingLot.Gentsuki;
        let price = parseInt(parkingLot.Price, 10);
        let uot = parseInt(parkingLot.Unit_of_Time, 10);
        let review = parseInt(parkingLot.Review, 10);

        if (lat && lon) {
                var markerOptions ={
                    riseOnHover: true,
                    riseOffset: 1000,
                    autoPanOnFocus: true
                }
                //L.marker([lat, lon],markerOptions).addTo(map)
                L.marker([lat, lon],markerOptions).addTo(markerLayerGroup)
                    .bindPopup(`
                        <b>${name}</b><br>Lat: ${lat}, Lon: ${lon}<br>
                        Availability: ${availability}<br>
                        Price: ${price} yen per ${uot} minutes<br>
                        <div id="details" style="display:none;">
                            Car: ${car}<br>
                            Bicycle: ${bike}<br>
                            Motorcycle: ${motor}<br>
                            Gentsuki: ${gentsuki}<br>
                            Review: ${review} Stars<br>
                        </div>
                        <br>
                        <button onclick="navigate(${lat}, ${lon}, document.getElementById('travel-mode-select').value)">Navigate Here</button>
                        <button id="detail_button" onclick="getDetailedContents()">Show Details</button>`);
        }
    });
}

function getDetailedContents()
{
    if(document.getElementById('details').getAttribute('style') == 'display:none;')
    {
        document.getElementById(`details`).setAttribute(`style`, `display:block;`);
        document.getElementById('detail_button').textContent = "Hide Details";
    }
    else
    {
        document.getElementById(`details`).setAttribute(`style`, `display:none;`);
        document.getElementById('detail_button').textContent = "Show Details";
    }
}


function navigate(lat, lon,travelMode) {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var userLocation = {
                    lat: position.coords.latitude,
                    lon: position.coords.longitude
                };

                getDirections(userLocation.lat, userLocation.lon, lat, lon,travelMode);
            },
            function(error) {
                alert('Error getting current location for navigation.');
            },
            {timeout: 10000, enableHighAccuracy: true, maximumAge: 0}
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
