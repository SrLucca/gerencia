from main.domain.posts.getaway.postGetaway import PostGateway
from main.domain.posts.entities.models import Post
from main.domain.posts.serializer.serializers import PostSerializer

class FindPostUseCase:
    #receber getaway
    def execute(self, id):
        getaway = PostGateway()
        post = getaway.find(id=id)
        return {'data': post.data}
        