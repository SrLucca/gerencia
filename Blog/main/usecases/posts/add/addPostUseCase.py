from main.domain.posts.getaway.postGetaway import PostGateway

class AddPostUseCase:
    
    def execute(post):
        new_post = PostGateway.save(post=post)
        return new_post
        