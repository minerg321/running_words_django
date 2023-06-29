from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # home 
    path('make_video/<str:text>/', views.MyView.as_view(), name='make_video'),
]
