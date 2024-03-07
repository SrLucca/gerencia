from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.views import APIView
from main.domain.posts.getaway.postGetaway import PostGateway
from .dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.usecases.posts.add.addPostUseCase import AddPostUseCase
from main.usecases.posts.list.listPostUseCase import ListPostUseCase
from main.usecases.posts.find.findPostUseCase import FindPostUseCase
class PostController(APIView):

    #Método post acessado pelo endpoint user
    def post(self, request):
        post_gateway = PostGateway()
        add_post_use_case = AddPostUseCase(post_gateway)

        serializer = AddPostRequestSerializer(data=request.data)
        if serializer.is_valid():
            post = add_post_use_case.execute(serializer.data)
            return Response(post)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #Método get acessado pelo endpoint user
    def get(self, request, pk=None):
        if pk is not None:
            use_case = FindPostUseCase()
            post = use_case.execute(pk)
            if post:
                return Response(post)
            return Response("Post not found", status=status.HTTP_404_NOT_FOUND)
        
        use_case = ListPostUseCase()
        posts = use_case.execute()
        return Response(posts)




