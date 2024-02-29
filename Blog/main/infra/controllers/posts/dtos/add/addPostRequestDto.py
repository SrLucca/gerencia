from rest_framework import serializers

class AddPostRequestSerializer(serializers.Serializer):
    title = serializers.CharField()
    author = serializers.CharField()
    content = serializers.CharField(style={'base_template': 'textarea.html'})
    created_at = serializers.TimeField()