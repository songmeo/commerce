from django.contrib import admin
from .models import Auction

# Register your models here.
class AuctionAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "price")
admin.site.register(Auction, AuctionAdmin)