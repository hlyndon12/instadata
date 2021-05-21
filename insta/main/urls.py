from django.urls import path
from .views import home, update,update_city

urlpatterns = [
    path('', home, name='home-view'),
    path('update/', update, name='update-view'),
    path('update/city/', update_city, name='update-city'),
]
