from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer

from .models import File
from .serializers import FileSerializer

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
def file_view(request):
    file = File('test')
    result = FileSerializer(file.__dict__)
    return Response(result.data)
