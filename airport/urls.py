from django.urls import path, include
from rest_framework import routers

from airport.views import (
    CrewViewSet, AirplaneTypeViewSet, AirplaneViewSet
)

router = routers.DefaultRouter()
router.register("crew", CrewViewSet)
router.register("airplane-type", AirplaneTypeViewSet)
router.register("airplane", AirplaneViewSet)

urlpatterns = [path("", include(router.urls))]

app_name = "airport"
