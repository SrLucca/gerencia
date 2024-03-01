from main.domain.users.getaway.userGetaway import UserGateway

class FindUserUseCase:

    def find(self, uuid):
        getaway = UserGateway()
        posts = getaway.list()
        return posts
        