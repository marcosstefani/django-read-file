from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    line = serializers.CharField(max_length=10000)

    def create(self, validated_data):
        return File(validated_data)

    def update(self, instance, validated_data):
        instance.line = validated_data.get('line', instance.line)
        return instance
