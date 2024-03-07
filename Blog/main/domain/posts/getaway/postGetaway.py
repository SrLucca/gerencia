from main.domain.posts.entities.models import Post
from main.domain.users.entities.models import User
from main.domain.posts.serializer.serializers import PostSerializer
from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from django.http import JsonResponse
from django.core.exceptions import ObjectDoesNotExist
import json
import uuid

class PostGateway:
    def save(self, post_data):
        if post_data.is_valid():
            post_data.save()
            return {'data': post_data.data, 'status': 201}
        else:
            return {'errors': 'Missing required data', 'status': 400}

    def find(self, id):
        try:
            post = Post.objects.get(id=id)
        except ObjectDoesNotExist:
            post = Post.objects.filter(author=id)
            return PostSerializer(post, many=True)
        return PostSerializer(post)