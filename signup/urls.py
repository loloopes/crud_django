from django.urls import path

from . import views

urlpatterns = [
    path('get_user/', views.get_User),
    path('create_user/', views.create_User),
    path('delete_user/', views.delete_User),
    path('patch_user/', views.update_user),
]
