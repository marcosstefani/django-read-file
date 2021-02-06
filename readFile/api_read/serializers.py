from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    content = serializers.CharField(max_length=10000)

    def create(self, validated_data):
        return File(validated_data)

    def update(self, instance, validated_data):
        instance.content = validated_data.get('content', instance.content)
        return instance
