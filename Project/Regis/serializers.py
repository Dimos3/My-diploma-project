from rest_framework import serializers
from .models import Admin
from rest_framework.renderers import JSONRenderer


class PRODUCKT:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class AdminSerial(serializers.Serializer):
    Name = serializers.CharField()
    Phone = serializers.CharField()
    #title = serializers.CharField(max_length=255)
    #content = serializers.CharField()

    #class Meta:
    #    model = Admin
    #    fields = ('Name','Phone')



def encode():
    model = PRODUCKT('Adonn','Content:935535')
    model_sr = AdminSerial(model)
    print(model_sr.data, type(model_sr.data), sep='\n')
    json = JSONRenderer().render(model_sr.data)
    print(json)

#class create(self, validated_data):
#    return Women.objects.create(**validated_data)