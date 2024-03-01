from main.domain.users.getaway.userGetaway import UserGateway

class ListUserUseCase:

    def find(self, id):
        getaway = UserGateway()
        user = getaway.find(id=id)
        return user
        