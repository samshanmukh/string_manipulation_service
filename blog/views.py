from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework import status

from .serializers import StringsSerializer
from .models import Strings

class StringsViewSet(viewsets.ModelViewSet):
   queryset = Strings.objects.all()
   serializer_class = StringsSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'list/': reverse('strings_list', request=request, format=format),
        'create/': reverse('strings_create', request=request, format=format),
        'get/': 'http://127.0.0.1:8000/api/get/1/',
        'update/': 'http://127.0.0.1:8000/api/update/1/',
        'delete/': 'http://127.0.0.1:8000/api/delete/1/',
        'string_operations/': 'http://127.0.0.1:8000/api/string_operations/1/',
    })


class ListStringsAPIView(ListAPIView):
    """This endpoint list all of the available Strings from the database"""
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer

class CreateStringsAPIView(CreateAPIView):
    """This endpoint allows for creation of a Strings"""
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer

class GetStringsAPIView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the Strings items for given requested user
        '''
        id = kwargs['id']
        strings = Strings.objects.filter(id = id)
        serializer = StringsSerializer(strings, many=True)
        return Response(serializer.data, status=200)

class UpdateStringsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific Strings by passing in the id of the Strings to update"""
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer

class DeleteStringsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Strings from the database"""
    queryset = Strings.objects.all()
    serializer_class = StringsSerializer


class StringOperationsAPIView(APIView):
    def put(self, request, *args, **kwargs):
        '''
        Updates the todo item with given todo_id if exists
        '''

        id = kwargs['id']
        string_instance = Strings.objects.filter(id = id).first()
        if not string_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        existingData = StringsSerializer(instance=string_instance).data

        # Input quqery
        content = request.body.decode('UTF-8')

        # String operations/manipulations
        if(content == 'sort'):
            out_string = ''.join(sorted(existingData['string']))
        if(content == 'reverse'):
            out_string = ''.join(reversed(existingData['string']))
        if(content == 'reverse_word'):
            out_string = ' '.join(reversed(existingData['string'].split(' ')))
        if(content == 'flip'):
            first_half = existingData['string'][0:len(existingData['string'])//2]
            second_half = existingData['string'][len(existingData['string'])//2:]
            out_string = second_half + first_half

        existingData['operations'][content] = out_string
        data = {
            'string': existingData['string'], 
            'operations': existingData['operations'],
        }
        serializer = StringsSerializer(instance = string_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

