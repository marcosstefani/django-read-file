from django.shortcuts import render
from rest_framework.decorators import api_view, renderer_classes, parser_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.parsers import MultiPartParser

from .models import File
from .serializers import FileSerializer
from .services import FileService

import json

# Create your views here.

@api_view(['PUT'])
@parser_classes([MultiPartParser])
@renderer_classes([JSONRenderer, XMLRenderer])
def random_line(request):
    content = []
    for i in request.data['text']:
        content.append(i.decode("utf-8").replace('\n', ''))
    service = FileService()
    file = File(service.random_line(content))
    result = FileSerializer(file.__dict__)
    return Response(result.data)