from django.urls import path
from . import views

urlpatterns = [
    path("categories/", views.CategoryList.as_view(), name=views.CategoryList.name),
    path(
        "categories/<pk>/",
        views.CategoryDetail.as_view(),
        name=views.CategoryDetail.name,
    ),
    path("drones/", views.DroneList.as_view(), name=views.DroneList.name),
    path("drones/<pk>/", views.DroneDetail.as_view(), name=views.DroneDetail.name),
    path("pilots/", views.PilotList.as_view(), name=views.PilotList.name),
    path("pilots/<pk>/", views.PilotDetail.as_view(), name=views.PilotDetail.name),
    path(
        "competitions/",
        views.CompetitionList.as_view(),
        name=views.CompetitionList.name,
    ),
    path(
        "competitions/<pk>/",
        views.CompetitionDetail.as_view(),
        name=views.CompetitionDetail.name,
    ),
    path("", views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
