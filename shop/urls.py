from django.urls import path
from rest_framework import routers
from .views import CityApiView, StreetApiView, StoreApiView

router = routers.SimpleRouter()
router.register(r'shop', StoreApiView)

urlpatterns = [
    path('city/', CityApiView.as_view()),
    path('<str:slug>/street/', StreetApiView.as_view()),
] + router.urls
