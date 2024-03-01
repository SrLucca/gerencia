from main.domain.posts.getaway.postGetaway import PostGateway

class AddUserUseCase:
    
    def execute(post):
        getaway = PostGateway()
        post = getaway.save(post=post)
        return post
        