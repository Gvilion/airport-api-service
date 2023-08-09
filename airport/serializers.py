from rest_framework import serializers

from airport.models import Crew, AirplaneType, Airplane


class CrewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Crew
        fields = ("id", "first_name", "last_name", "full_name")


class AirplaneTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AirplaneType
        fields = ("id", "name")


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = (
            "id", "name", "rows", "seats_in_row", "capacity", "airplane_type"
        )


class AirplaneListSerializer(AirplaneSerializer):
    airplane_type = serializers.SlugRelatedField(read_only=True,
                                                 slug_field="name")
