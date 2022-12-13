from django.contrib import admin
from .models.restaurant import FoodType, PaymentOptions, Restaurant, RestaurantGalleryPhoto

# Register your models here.
admin.site.register(FoodType)
admin.site.register(PaymentOptions)
admin.site.register(Restaurant)
admin.site.register(RestaurantGalleryPhoto)
