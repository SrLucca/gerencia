from main.domain.posts.getaway.postGetaway import PostGateway
from main.domain.posts.entities.models import Post
from main.domain.posts.serializer.serializers import PostSerializer
from main.domain.users.entities.models import User

class AddPostUseCase:
    def __init__(self, post_gateway):
        self.post_gateway = post_gateway

    def execute(self, post):
        last_author = User.objects.last()  # Supondo que User.objects seja um queryset de usuários
        new_post = {
            'title': post['title'],
            'author': last_author.id,
            'content': post['content']
        }
        serializer = PostSerializer(data=new_post)
        return self.post_gateway.save(serializer)
        