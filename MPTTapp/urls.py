from MPTTapp import views
from django.urls import path

urlpatterns = [
    path('', views.showfilesorfolder,name='homepage'),
]
