from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("", ListView.as_view(), name="ListView"),
    path("add/", CreateView.as_view(), name="add"),
    path("<slug:pk>", DetailView.as_view(), name="detail"),
    path("<slug:pk>/update", UpdateView.as_view(), name="update"),
    path("<slug:pk>/delete", DeleteView.as_view(), name="delete")
]
