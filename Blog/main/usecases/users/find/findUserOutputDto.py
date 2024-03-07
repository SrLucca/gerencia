from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from main.domain.users.serializer.serializers import UserSerializer

class FindserUseCase:
    
    #Método de criacao de usuario usecase <-> getaway 
    def execute(user):
        try:
            find_user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return {'user': serializer.data}
        except User.DoesNotExist:
            return None
