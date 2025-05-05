from django.db import models
from django.contrib.auth.models import User



class ParkingLot(models.Model):
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()
    picture = models.ImageField(upload_to='./parking_lot_pictures/')
    vehicle_type = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)  # Define a default value
    unit_of_time = models.CharField(max_length=255)
    reviews = models.TextField(default="")
    current_free_spot = models.IntegerField(default=0)

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

class RegisteredUser(User):
    points = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    warnings = models.IntegerField(default=0)
    report = models.TextField(blank=True)

    def leave_comment(self, parking: ParkingLot) -> bool:
        # Implement logic to leave a comment on parking
        return True

    def report_info(self, parking: ParkingLot) -> bool:
        # Implement logic to report info on parking
        return True

    def upload_parking(self, parking: ParkingLot) -> bool:
        # Implement logic to upload parking
        return True

    def edit_parking(self, parking: ParkingLot) -> bool:
        # Implement logic to edit parking
        return True

    def leave_review(self, parking: ParkingLot, rating: float, comment: str) -> bool:
        # Implement logic to leave a review on parking
        return True

    def __str__(self):
        return self.name