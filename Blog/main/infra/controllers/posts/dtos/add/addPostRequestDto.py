from rest_framework import serializers

class AddPostRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_lenght=255)
    author = serializers.CharField(max_lenght=255)
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    created_at = serializers.TimeField()