from rest_framework.response import Response
from rest_framework.views import APIView
from main.infra.controllers.posts.dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.infra.controllers.users.dtos.add.addUserRequestDto import AddUserRequestSerializer
from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from main.usecases.posts.add.addPostUseCase import AddPostUseCase


class UserPostController(APIView):

    def post(self, request):
        getaway = UserGateway()
        data = {'title': request.query_params.get('title'), 
                'content': request.query_params.get('content')}
        serializer = AddPostRequestSerializer(data=data)
        if serializer.is_valid():
            new_post = AddPostUseCase.execute(serializer.data)
            return Response(new_post)
        return Response(serializer.errors)
