from rest_framework import serializers
from .models import File

class FileSerializer(serializers.Serializer):
    line = serializers.CharField(max_length=10000)
    highest_occurrence = serializers.CharField(max_length=1)

    def create(self, validated_data):
        return File(validated_data)

    def update(self, instance, validated_data):
        instance.line = validated_data.get('line', instance.line)
        instance.highest_occurrence = validated_data.get('highest_occurrence', instance.highest_occurrence)
        return instance
