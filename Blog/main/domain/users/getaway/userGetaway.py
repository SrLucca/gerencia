from entities.models import User
from serializer.serializers import UserSerializer
from django.http import JsonResponse

class UserGateway:
    def save(self, user):
        #utiliza o metodo create do modelo
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    def find(self, id):
        try:
            user = Post.objects.get(id=id)
            serializer = UserSerializer(user)
            return JsonResponse(serializer.data)
        except User.DoesNotExist:
            return None

    def list(self):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return JsonResponse(serializer.data, safe=False)