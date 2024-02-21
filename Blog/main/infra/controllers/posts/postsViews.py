from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from dtos.add.addPostRequestDto import AddPostRequestSerializer
from main.usecases.posts.add.addPostUseCase import AddPostUseCase
class PostController(APIView):

    @api_view(['POST'])
    def addPost(request):
        serializer = AddPostRequestSerializer(data=request.data)
        if serializer.is_valid():
            post = AddPostUseCase.execute(serializer.data)
            return Response(post)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(['GET'])
    def listPost(request):
        return
