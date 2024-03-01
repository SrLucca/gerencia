from django.urls import path
from rest_framework import routers
from main.infra.controllers.posts.postsViews import PostController
from main.infra.controllers.users.userViews import UserController
from main.infra.controllers.users.userPostViews import UserPostController

urlpatterns = [
    path('post', PostController.as_view(), name="list-posts"),
    path('user', UserController.as_view(), name="list-users"),
    path('user/add', UserController.as_view(), name="add-user"),
    path('user/add/post', UserPostController.as_view(), name='add-post'),
]