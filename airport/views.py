from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from airport.models import Crew, AirplaneType, Airplane
from airport.serializers import (
    CrewSerializer,
    AirplaneListSerializer,
    AirplaneTypeSerializer,
    AirplaneSerializer
)


class CrewViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer


class AirplaneTypeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = AirplaneType.objects.all()
    serializer_class = AirplaneTypeSerializer


class AirplaneViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Airplane.objects.all()
    serializer_class = AirplaneSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return AirplaneListSerializer

        return AirplaneSerializer
