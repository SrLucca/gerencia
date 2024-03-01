from main.domain.posts.getaway.postGetaway import PostGateway

class AddPostUseCase:
    
    def execute(post):
        getaway = PostGateway()
        new_post = getaway.save(post=post)
        return new_post
        