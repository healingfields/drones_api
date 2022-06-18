from asyncio import mixins
from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Drone, Competition, Category, Pilot
from .serializers import (
    CompetitionSerializer,
    DroneSerializer,
    CategorySerializer,
    PilotCompetitionSerializer,
    PilotSerializer,
)


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = "category-list"


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    name = "category-detail"


class DroneList(generics.ListCreateAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-list"


class DroneDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Drone.objects.all()
    serializer_class = DroneSerializer
    name = "drone-detail"


class PilotList(generics.ListCreateAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-list"


class PilotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pilot.objects.all()
    serializer_class = PilotSerializer
    name = "pilot-detail"


class CompetitionList(generics.ListCreateAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-list"


class CompetitionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Competition.objects.all()
    serializer_class = PilotCompetitionSerializer
    name = "competition-detail"


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response(
            {
                "categories": reverse(CategoryList.name, request=request),
                "drones": reverse(DroneList.name, request=request),
                "pilots": reverse(PilotList.name, request=request),
                "competitions": reverse(CompetitionList.name, request=request),
            }
        )
