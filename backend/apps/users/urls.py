from django.urls import path, include
from rest_framework import routers
from .views import (
    UserViewSet, SubmissionsViewSet, CustomAuthToken, UserProfileView
)

router = routers.SimpleRouter()
router.register(r'', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]