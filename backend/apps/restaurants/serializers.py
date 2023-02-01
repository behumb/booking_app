from rest_framework import serializers
from .models import FoodType, PaymentOptions, Restaurant, RestaurantGalleryPhoto


class FoodTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodType
        fields = ('id', 'name')


class PaymentOptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentOptions
        fields = ('id', 'name')


class RestaurantGalleryPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestaurantGalleryPhoto
        fields = ('id', 'short_name', 'image')


class RestaurantSerializer(serializers.ModelSerializer):
    photos = RestaurantGalleryPhotoSerializer(many=True)
    food_type = FoodTypeSerializer()
    payment_options = PaymentOptionsSerializer(many=True)
    class Meta:
        model = Restaurant
        fields = '__all__'
