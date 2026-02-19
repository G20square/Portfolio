from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact_submit, name='contact'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add-project/', views.add_project, name='add_project'),
    path('edit-project/<int:pk>/', views.edit_project, name='edit_project'),
    path('delete-project/<int:pk>/', views.delete_project, name='delete_project'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('add-skill/', views.add_skill, name='add_skill'),
    path('edit-skill/<int:pk>/', views.edit_skill, name='edit_skill'),
    path('delete-skill/<int:pk>/', views.delete_skill, name='delete_skill'),
]
