from main.domain.posts.getaway.postGetaway import PostGateway

class AddUserUseCase:
    
    #Método de criacao de usuario/post usecase <-> getaway 
    def execute(post):
        getaway = PostGateway()
        post = getaway.save(post=post)
        return post
        