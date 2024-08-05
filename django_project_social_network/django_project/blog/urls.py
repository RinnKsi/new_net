from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='posts'),
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
    path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
    path('about/', views.about, name='about'),
    path('add_music/', views.MusicCreateView.as_view(), name='add_music'),
    path('music_list/', views.MusicListView.as_view(), name='music_list'),
]
