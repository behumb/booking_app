from django.db import models
from services.restaurant_service import restaurant_directory_path


class FoodType(models.Model):
    name = models.CharField('TypeName', max_length=50)


class PaymentOptions(models.Model):
    name = models.CharField('PaymentName', max_length=30)


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
        on_delete=models.SET_DEFAULT,
        default=FoodType.objects.get(name='International').pk)
    payment_options = models.ManyToManyField(PaymentOptions)
    additional = models.CharField('Additional', max_length=150)
    main_photo = models.ImageField(upload_to=restaurant_directory_path)


class RestaurantGalleryPhoto(models.Model):
    image = models.ImageField(upload_to=restaurant_directory_path)
    restaurant = models.ForeignKey(Restaurant, related_name='photos', on_delete=models.CASCADE)
