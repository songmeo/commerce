from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    def __str__(self):
        return f"{self.username}"

class Auction(models.Model):
    name = models.CharField(max_length=64)
    price = models.FloatField(default=0)
    def __str__(self):
        return f"{self.name} costs {self.price}"

class Bid(models.Model):
    price = models.FloatField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bid")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="bids")
    
    def __str__(self):
        return f"{self.user} bids {self.price} for {self.auction}"

class Comment(models.Model):
    comment = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment")
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE, related_name="comments")
    
    def __str__(self):
        return f"{self.user} commented: {self.comment} about {self.auction}"