from django.urls import path
from . import views

urlpatterns = [
    path('user-create/', views.UserCreate.as_view()),
    path('home/<int:pk>/', views.HomeView.as_view()),
]
