from django.urls import path
from . import views

"""
This file defines the URL patterns for the catalog app.

Each URL pattern is associated with a view function that handles the request and response cycle.
"""

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:pk>/', views.edit_product, name='edit_product'),
    path('delete/<int:pk>/', views.delete_product, name='delete_product'),
]