from rest_framework import serializers
from .models import ApiTemplate


class ApiTemplateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTemplate
        fields = "__all__"


class ApiTemplateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiTemplate
        fields = ("id", "body")
