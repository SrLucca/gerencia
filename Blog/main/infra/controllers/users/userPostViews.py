from rest_framework.response import Response
from rest_framework.views import APIView
from main.infra.controllers.posts.dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.infra.controllers.users.dtos.add.addUserRequestDto import AddUserRequestSerializer
from main.domain.users.getaway.userGetaway import UserGateway
from main.usecases.users.find.findUserUseCase import FindUserUseCase
from main.domain.users.entities.models import User
from main.usecases.posts.add.addPostUseCase import AddPostUseCase
from main.usecases.posts.find.findPostUseCase import FindPostUseCase


class UserPostController(APIView):

    def post(self, request):
        post_gateway = UserGateway()
        add_user_post_use_case = AddPostUseCase(post_gateway)

        data = {'title': request.query_params.get('title'), 
                'content': request.query_params.get('content')}
        serializer = AddPostRequestSerializer(data=data)

        if serializer.is_valid():
            new_post = add_user_post_use_case.execute(serializer.data)
            return Response(new_post)
        return Response(serializer.errors)

    def get(self, request, pk=None):
        if pk is not None:
            use_case = FindPostUseCase()
            post = use_case.execute(pk)
            if post:
                return Response(post)
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)

