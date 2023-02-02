from django.db import models
from .services import restaurant_directory_path


class FoodType(models.Model):
    name = models.CharField('TypeName', max_length=50, unique=True)

    def __str__(self):
        return self.name


class PaymentOptions(models.Model):
    name = models.CharField('PaymentName', max_length=30, unique=True)

    def __str__(self):
        return self.name


class Restaurant(models.Model):
    name = models.CharField('Name', max_length=50)
    description = models.TextField('Description')
    min_sum = models.FloatField('MinSum')
    max_sum = models.FloatField('MaxSum', default=None)
    website = models.CharField('Website', max_length=100)
    phone = models.CharField('Phone', max_length=20)
    parking_detail = models.CharField('ParkingDetail', max_length=100)
    food_type = models.ForeignKey(
        FoodType,
        related_name='restaurants',
        on_delete=models.CASCADE)
    payment_options = models.ManyToManyField(PaymentOptions)
    additional = models.CharField('Additional', max_length=150)
    main_photo = models.ImageField('MainPhoto', upload_to=restaurant_directory_path)

    def __str__(self):
        return self.name


class RestaurantGalleryPhoto(models.Model):
    short_name = models.CharField('PhotoName', max_length=30)
    image = models.ImageField('URL', upload_to=restaurant_directory_path)
    restaurant = models.ForeignKey(Restaurant, related_name='photos', on_delete=models.CASCADE)

    def __str__(self):
        return self.short_name
