"""snacks_crud_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import (
    SnackListView,
    SnackDetailView,
    SnackCreateView,
    SnackUpdateView,
    SnackDeleteView,

    )

urlpatterns = [
    path('', SnackListView.as_view(),name="snack-list"),
    path('<int:pk>/',SnackDetailView.as_view(),name="snack-detail"),
    path('create/',SnackCreateView.as_view(),name="snack-create"),
    path('<int:pk>/update/',SnackUpdateView.as_view(),name="snack-update"),
    path('<int:pk>/delete/',SnackDeleteView.as_view(),name="snack-delete")
    
]
