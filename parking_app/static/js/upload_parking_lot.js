// static/js/upload_parking_lot.js

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('uploadForm').addEventListener('submit', function(event) {
        event.preventDefault();
        var formData = new FormData(this);

        fetch('/upload_parking_lot/', {
            method: 'POST',
            body: formData
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                alert('Parking lot uploaded successfully!');
                document.getElementById('uploadModal').style.display = 'none';
            } else {
                alert('Error uploading parking lot.');
            }
        })
        .catch(error => {
            console.error('Error uploading parking lot:', error);
        });
    });
});

function locateParkingLot() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            function(position) {
                var lat = position.coords.latitude;
                var lon = position.coords.longitude;
                document.getElementById('latitude').value = lat;
                document.getElementById('longitude').value = lon;

                // Add marker to the map
                L.marker([lat, lon]).addTo(map)
                    .bindPopup('New Parking Lot Location').openPopup();

                map.setView([lat, lon], 16);
            },
            function(error) {
                alert('Error getting current location.');
            },
            {timeout: 10000, enableHighAccuracy: true, maximumAge: 0}
        );
    } else {
        alert("Geolocation is not supported by this browser.");
    }
}
