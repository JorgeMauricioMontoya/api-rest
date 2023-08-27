from django.test import TestCase
from .models import Project

# Create your tests here.
class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        field = ("id", "title", "description", "technology", "created_at")