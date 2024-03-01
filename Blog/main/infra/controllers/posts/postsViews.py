from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from .dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.usecases.posts.add.addPostUseCase import AddPostUseCase
from main.usecases.posts.list.listPostUseCase import ListPostUseCase
class PostController(APIView):

    def post(self, request):
        serializer = AddPostRequestSerializer(data=request.data)
        if serializer.is_valid():
            post = AddPostUseCase.execute(serializer.data)
            return Response(post)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        use_case = ListPostUseCase()
        posts = use_case.list()
        return Response(posts)
