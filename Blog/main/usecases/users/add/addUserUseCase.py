from main.domain.users.getaway.userGetaway import UserGateway

class AddUserUseCase:
    
    def execute(user):
        user = UserGateway.save(user=user)
        return user
        