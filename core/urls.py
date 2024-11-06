from django.urls import path
from .views.v1.api_views import HomeView, ImageModelView

urlpatterns = [
    path('v1/hello/', HomeView.as_view(), name='hello_world'),
    path('v1/images/', ImageModelView.as_view(), name='image_view'),
]