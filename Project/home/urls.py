
from django.urls import path
from .views import TestAPIView

app_name = 'home'
urlpatterns = [
    path('api/test/<int:number>/', TestAPIView.as_view(), name='test_api'),
]
