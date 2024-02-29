from main.domain.posts.getaway.postGetaway import PostGateway

class ListPostUseCase:
    
    def find(self, id):
        getaway = PostGateway()
        post = getaway.find(id=id)
        return post

    def list(self):
        getaway = PostGateway()
        posts = getaway.list()
        return posts
        