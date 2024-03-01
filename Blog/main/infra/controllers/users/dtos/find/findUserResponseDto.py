from rest_framework import serializers
from main.domain.users.entities.models import User
from main.infra.controllers.users.dtos.find.FindUserRequestDto import FindUserRequestSerializer
class FindUserResponse:

    def find(self, uuid):
        try:
            # Busca o usuário pelo UUID
            user = User.objects.get(id=uuid)
        except User.DoesNotExist:
            return Response({"message": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = FindUserRequestSerializer(user)

        # Retorna a resposta serializada
        return Response(serializer.data, status=status.HTTP_200_OK)