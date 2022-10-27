from django.urls import path

from . import views

urlpatterns = (
    path('users', views.user_list),
    path('user/<int:id>/', views.user_view),
    path('user/<int:id>/edit/', views.user_edit),
    path('user/<int:id>/posts/', views.user_posts),
    path('user/<int:id>/folders/', views.user_folders),
    path('post/new/', views.post_new),
    path('post/<int:id>/', views.post_view),
    path('post/<int:id>/edit/', views.post_edit),
    path('folders/', views.folder_list),
    path('folder/new/', views.folder_new),
    path('folder/<int:id>/', views.folder_view),
    path('folder/<int:id>/edit', views.folder_edit),
    path('login/', views.login),
    path('role/<int:id>/', views.role_view)
)
