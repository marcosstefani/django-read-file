from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, parser_classes, renderer_classes
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework_xml.renderers import XMLRenderer
from rest_framework.parsers import MultiPartParser, JSONParser

from .models import File
from .serializers import FileSerializer
from .services import FileService

# Create your views here.

@api_view(['PUT'])
@parser_classes([MultiPartParser])
@renderer_classes([JSONRenderer, XMLRenderer])
def random_line(request):
    content = []
    for i in request.data['text']:
        content.append(i.decode("utf-8").replace('\n', ''))
    service = FileService()
    line = service.random_line(content)
    file = File(line, service.highest_occurrence(line))
    result = FileSerializer(file.__dict__)
    return Response(result.data)
