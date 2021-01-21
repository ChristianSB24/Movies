# app/movies/views.py

from rest_framework import viewsets
from django.http import Http404
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Movie
from .serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
   
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

    def list(self, request):
    	pass

    def create(self, request):
    	pass

    def retrieve(self, request, pk=None):
    	pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
    	pass

    
