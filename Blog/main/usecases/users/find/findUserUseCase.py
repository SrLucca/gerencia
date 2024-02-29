from main.domain.users.getaway.userGetaway import UserGateway

class ListUserUseCase:
    
    def find(id):
        user = UserGateway.find(id=id)
        return user

    def list():
        users = UserGateway.list()
        return users
        