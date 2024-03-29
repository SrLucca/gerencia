from main.domain.posts.getaway.postGetaway import PostGateway
from main.domain.posts.entities.models import Post
from main.domain.posts.serializer.serializers import PostSerializer

class ListPostUseCase:

    def execute(self):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return {'data': serializer.data}
        