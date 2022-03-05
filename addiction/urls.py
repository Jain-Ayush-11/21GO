from django.urls import path
from . import views

urlpatterns = [
    path('user-create/', views.UserCreate.as_view()),
    path('home/<int:pk>/', views.HomeView.as_view()),
    path('wallpapers/<int:pk>/', views.WallpaperGet.as_view()),
    path('exit/<int:pk>/', views.ExitView.as_view()),
    path('relapse-record/', views.RelapseRecord.as_view()),
    path('relapse/<int:pk>/', views.CalenderStats.as_view()),
    path('post/', views.PostView.as_view()),
]
