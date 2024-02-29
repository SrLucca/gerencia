from rest_framework import serializers
from main.domain.posts.entities.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'