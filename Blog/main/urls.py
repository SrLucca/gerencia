from django.urls import path
from main.infra.controllers.posts.postsViews import PostController
urlpatterns = [
    path('post/', PostController.as_view(), name="list_posts")
]