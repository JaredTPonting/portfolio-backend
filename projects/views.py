from django.http import JsonResponse
from rest_framework import viewsets

from .models import Project, Tag
from .serializers import ProjectSerializer, TagSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer