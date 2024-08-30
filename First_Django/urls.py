from django.contrib import admin
from django.urls import path
from MainApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('about', views.about, name="about"),
    path('items', views.item, name="items"),
    path('item/<int:id_>', views.item_id, name="item_id")
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
