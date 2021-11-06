from rest_framework import serializers

from .models import Strings


class StringsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Strings
       fields = ('id', 'string', 'operations', 'createdAt', 'updatedAt')