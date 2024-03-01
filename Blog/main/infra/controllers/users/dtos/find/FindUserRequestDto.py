from rest_framework import serializers
from main.domain.posts.entities.models import User

class FindUserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
