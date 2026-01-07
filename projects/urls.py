from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from .views import TagViewSet, ProjectViewSet

router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('projects', ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
]