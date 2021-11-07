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
        'get/': 'https://string-manipulation-service.herokuapp.com/api/get/4/',
        'update/': 'https://string-manipulation-service.herokuapp.com/api/update/4/',
        'delete/': 'https://string-manipulation-service.herokuapp.com/api/delete/4/',
        'string_operations/': 'https://string-manipulation-service.herokuapp.com/api/string_operations/4/',
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
    def get_object(self, id):
        '''
        Helper method to get the object with given id
        '''
        try:
            return Strings.objects.get(id=id)
        except Strings.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        '''
        Updates the string item with given id if exists
        '''

        id = kwargs['id']
        # string_instance = Strings.objects.filter(id = id).first()
        string_instance = self.get_object(id)
        if not string_instance:
            return Response(
                {"res": "Object with id does not exists"}, 
                status=status.HTTP_400_BAD_REQUEST
            )
        existingData = StringsSerializer(instance=string_instance).data

        # Options - sort, reverse, reverse_word, flip
        # Request body
        content = request.body.decode('UTF-8')
        if not content:
            return Response(
                {"res": "Empty request object"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

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

