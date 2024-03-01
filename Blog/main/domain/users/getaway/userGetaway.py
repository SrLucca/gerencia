from main.domain.users.entities.models import User
from main.domain.users.serializer.serializers import UserSerializer

class UserGateway:
    def save(self, user):
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return {'data': serializer.data, 'status': 201}
        return {'errors': serializer.errors, 'status': 400}

    def find(self, id):
        try:
            user = User.objects.get(id=id)
            serializer = UserSerializer(user)
            return {'user': serializer.data}
        except User.DoesNotExist:
            return None

    def list(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return {'data': serializer.data}