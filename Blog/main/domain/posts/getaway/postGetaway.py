from posts.entities.models import Post

class PostGateway:
    def save(self, post):
        post.save()

    def find(self, id):
        try:
            return Post.objects.get(id=id)
        except Post.DoesNotExist:
            return None

    def list(self):
        return Post.objects.all()