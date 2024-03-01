from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .dtos.add.addUserRequestDto import AddUserRequestSerializer
from main.infra.controllers.posts.dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.domain.users.getaway.userGetaway import UserGateway
from main.domain.users.entities.models import User
from main.usecases.users.add.addUserUseCase import AddUserUseCase
from main.usecases.posts.add.addPostUseCase import AddPostUseCase
from main.usecases.users.list.listUserUseCase import ListUserUseCase

class UserController(APIView):

    def post(self, request):
        data = {'name': request.query_params.get('name'), 
                'email': request.query_params.get('email')}

        serializer = AddUserRequestSerializer(data=data)
        if serializer.is_valid():
            user = AddUserUseCase.execute(serializer.data)
            return Response(user)
        return Response(serializer.errors)

    def get(self, request):
        use_case = ListUserUseCase()
        users = use_case.list()
        return Response(users)
