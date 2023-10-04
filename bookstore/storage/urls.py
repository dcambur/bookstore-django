from django.urls import path
from . import views

urlpatterns = [
    path("get/", views.store_list)
]