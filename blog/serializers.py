from rest_framework import serializers

from .models import Strings


class StringsSerializer(serializers.ModelSerializer):
   class Meta:
       model = Strings
       fields = '__all__'