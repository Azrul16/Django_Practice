from rest_framework import serializers



class MovieSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    active = serializers.BooleanField()
    

