from main.domain.posts.entities.models import Post
from main.domain.users.entities.models import User
from main.domain.posts.serializer.serializers import PostSerializer
from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from django.http import JsonResponse
import json
import uuid

class PostGateway:
    def save(self, post):
        last_author = User.objects.last()
        new_post = {
            'title':post['title'],
            'author': last_author.id,
            'content': post['content']
        }
        serializer = PostSerializer(data=new_post)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return {'data': serializer.data, 'status': 201}
        return {'errors': serializer.errors, 'status': 400}

    def find(self, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return {'data': serializer.data}
        except User.DoesNotExist:
            return None

    def list(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return {'data': serializer.data}