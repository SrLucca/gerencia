from rest_framework import serializers

class AddPostRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    content = serializers.CharField()