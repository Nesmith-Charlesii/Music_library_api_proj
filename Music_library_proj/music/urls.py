from django.urls import path
from . import views

urlpatterns = [
    path('music/', views.SongList.as_view()),
    path('music/<int:song_id>/', views.SongDetail.as_view())
]
