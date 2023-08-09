from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from airport.models import Crew
from airport.serializers import CrewSerializer


class CrewViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = Crew.objects.all()
    serializer_class = CrewSerializer
