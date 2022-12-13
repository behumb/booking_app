from rest_framework import status, viewsets, mixins
from apps.restaurants.models import FoodType, PaymentOptions, RestaurantGalleryPhoto, Restaurant
from serializers.restaurant import FoodTypeSerializer, PaymentOptionsSerializer, RestaurantGalleryPhotoSerializer, \
    RestaurantSerializer


class FoodTypeViewSet(mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      viewsets.GenericViewSet):
    serializer_class = FoodTypeSerializer
    queryset = FoodType.objects.all()


class PaymentOptionsViewSet(mixins.RetrieveModelMixin,
                            mixins.ListModelMixin,
                            viewsets.GenericViewSet):
    serializer_class = PaymentOptionsSerializer
    queryset = PaymentOptions.objects.all()


class RestaurantGalleryPhotoViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantGalleryPhotoSerializer
    queryset = RestaurantGalleryPhoto.objects.all()


class RestaurantViewSet(viewsets.ModelViewSet):
    serializer_class = RestaurantSerializer
    queryset = Restaurant.objects.all()
