from django.shortcuts import render

from rest_framework import viewsets

from .serializers import StringsSerializer
from .models import Strings

class StringsViewSet(viewsets.ModelViewSet):
   queryset = Strings.objects.all()
   serializer_class = StringsSerializer
