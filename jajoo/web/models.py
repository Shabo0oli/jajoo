from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from location_field.models.plain import PlainLocationField


# Create your models here.


class UserInfo(models.Model):
    Username = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone = PhoneNumberField()
    Avatar = models.ImageField(upload_to='web/static/avatar/', default='web/static/avatar/default.png')

    def __str__(self):
        return "{} : {}".format(self.Username, self.Phone)


class Place(models.Model):
    CostPerDay = models.IntegerField(default=0)
    Owner = models.ForeignKey(User, on_delete=models.CASCADE)
    Address = models.TextField(max_length=500)
    Location = PlainLocationField(based_fields=['Address'], zoom=7)
    Bedroom = models.IntegerField(default=0)
    HasParking = models.BooleanField(default=False)
    HasWifi = models.BooleanField(default=False)
    HasBath = models.BooleanField(default=False)
    HasTv = models.BooleanField(default=False)
    Pic = models.ImageField(upload_to='web/static/homepicture/', default='web/static/homepicture/default.png')

    def __str__(self):
        return "{} : ({})".format(self.Owner.username, self.Address)


class Booking(models.Model):
    CheckInDate = models.DateTimeField()
    CheckOutDate = models.DateTimeField()
    Guest = models.ForeignKey(User, on_delete=models.CASCADE)
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)

    STATUS_OPTIONS = (
        ('Pending', 'Pending'),
        ('Accept', 'Accept'),
        ('Reject', 'Reject'),
    )
    Status = models.CharField(max_length=20, choices=STATUS_OPTIONS, default='Pending')

    def __str__(self):
        return "{} : {} : {} - {}".format(self.Guest, self.Place, self.CheckInDate, self.CheckOutDate)


class Comment(models.Model):
    Text = models.TextField(max_length=200)
    CreationDate = models.DateTimeField(auto_now_add=True, blank=True)
    Writer = models.ForeignKey(User, on_delete=models.CASCADE)
    Place = models.ForeignKey(Place, on_delete=models.CASCADE)

    def __str__(self):
        return "{} : {} : {} : {}".format(self.Writer, self.Place, self.Text, self.CreationDate)


