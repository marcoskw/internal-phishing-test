from django.urls import path
from . import views

urlpatterns = [
    path('click/', views.click_link, name='click_link'),
]