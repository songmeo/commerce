from django.contrib import admin
from .models import Auction, Bid, User

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created", "category", "price", "description")
admin.site.register(Auction, AuctionAdmin)
admin.site.register(Bid)
admin.site.register(User)