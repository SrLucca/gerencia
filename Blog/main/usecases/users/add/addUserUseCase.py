from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from main.domain.users.serializer.serializers import UserSerializer

class AddUserUseCase:
    def __init__(self, user_gateway):
        self.user_gateway = user_gateway
    #Método de criacao de usuario usecase <-> getaway 
    def execute(self, user):
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            self.user_gateway.save(serializer)
            return {'data': serializer.data, 'status': 201}
        return {'errors': serializer.errors, 'status': 400}

        