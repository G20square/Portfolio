from django.urls import path
from .api_views import ProjectListCreateView, ProjectDetailView, ContactCreateView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='api-project-list'),
    path('projects/<slug:slug>/', ProjectDetailView.as_view(), name='api-project-detail'),
    path('contact/', ContactCreateView.as_view(), name='api-contact-create'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'),
]
