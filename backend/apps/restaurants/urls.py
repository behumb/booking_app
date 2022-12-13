from rest_framework.routers import SimpleRouter
from views.restaurants import FoodTypeViewSet, PaymentOptionsViewSet, RestaurantViewSet, RestaurantGalleryPhotoViewSet

router = SimpleRouter()
router.register(r'food_types', FoodTypeViewSet, basename='food_types')
router.register(r'payment_options', PaymentOptionsViewSet, basename='payment_options')
router.register(r'', RestaurantViewSet, basename='restaurants')
router.register(r'restaurants_gallery', RestaurantGalleryPhotoViewSet, basename='restaurants_gallery')

urlpatterns = []

urlpatterns += router.urls
