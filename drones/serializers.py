from rest_framework import serializers
from drones.models import Drone, Category, Pilot, Competition
from . import views


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    drones = serializers.HyperlinkedRelatedField(
        many=True, read_only=True, view_name="drone-detail"
    )

    class Meta:
        model = Category
        fields = ("url", "pk", "name", "drones")


class DroneSerializer(serializers.HyperlinkedModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field="name"
    )

    class Meta:
        model = Drone
        fields = (
            "url",
            "name",
            "category",
            "manufacturing_date",
            "has_it_competed",
            "created",
        )


class CompetitionSerializer(serializers.HyperlinkedModelSerializer):
    drone = DroneSerializer(many=False)

    class Meta:
        model = Competition
        fields = ("url", "pk", "distance_in_feet", "distance_achievement_date", "drone")


class PilotSerializer(serializers.HyperlinkedModelSerializer):
    competitions = CompetitionSerializer(many=True, read_only=True)
    gender = serializers.ChoiceField(choices=Pilot.GENDER_CHOICES)
    gender_description = serializers.CharField(
        source="get_gender_display", read_only=True
    )

    class Meta:
        model = Pilot
        fields = (
            "url",
            "name",
            "gender",
            "gender_description",
            "races_count",
            "created",
            "competitions",
        )


class PilotCompetitionSerializer(serializers.ModelSerializer):
    pilot = serializers.SlugRelatedField(
        queryset=Pilot.objects.all(), slug_field="name"
    )
    drone = serializers.SlugRelatedField(
        queryset=Drone.objects.all(), slug_field="name"
    )

    class Meta:
        model = Competition
        fields = (
            "url",
            "pk",
            "distance_in_feet",
            "distance_achievement_date",
            "pilot",
            "drone",
        )
