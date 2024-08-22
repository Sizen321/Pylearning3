from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about', views.about),
    path('items', views.item),
    path('item/<int:id_>', views.item_id)
]
