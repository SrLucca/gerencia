from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from main.domain.users.serializer.serializers import UserSerializer

class ListUserUseCase:
    
    #Método de criacao de usuario usecase <-> getaway 
    def execute(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return {'data': serializer.data}

