from main.domain.users.getaway.userGetaway import UserGateway

class AddUserUseCase:
    
    def execute(user):
        getaway = UserGateway()
        user = getaway.save(user=user)
        return user
        