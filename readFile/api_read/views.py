from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.parsers import MultiPartParser

from .models import File
from .serializers import FileSerializer

# Create your views here.

@api_view(['GET'])
@renderer_classes([JSONRenderer, XMLRenderer])
def file_view(request):
    file = File('test')
    result = FileSerializer(file.__dict__)
    return Response(result.data)

@api_view(['PUT'])
@parser_classes([MultiPartParser])
@renderer_classes([JSONRenderer, XMLRenderer])
def random_line(request):
    file_obj = request.FILES
    print(file_obj)
    print(request.data)
    return Response({'received data': request.data})