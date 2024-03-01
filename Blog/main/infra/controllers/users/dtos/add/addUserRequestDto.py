from rest_framework import serializers

class AddUserRequestSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.CharField()
