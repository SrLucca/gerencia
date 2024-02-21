from posts.entities.models import Post
from serializer.serializers import PostSerializer
from django.http import JsonResponse

class PostGateway:
    def save(self, post):
        #utiliza o metodo create do modelo
        serializer = PostSerializer(data=post)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def find(self, id):
        try:
            post = Post.objects.get(id=id)
            serializer = PostSerializer(post)
            return JsonResponse(serializer.data)
        except Post.DoesNotExist:
            return None

    def list(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)