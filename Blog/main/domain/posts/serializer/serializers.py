from rest_framework import serializers
from main.domain.posts.entities.models import Post
from main.domain.users.entities.models import User
from rest_framework import serializers

# "DTO" do post (serializacao) 
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'