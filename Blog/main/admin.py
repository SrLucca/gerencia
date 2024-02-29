from django.contrib import admin
from main.domain.posts.entities.models import Post
from main.domain.users.entities.models import User
# Register your models here.

admin.site.register(Post)
admin.site.register(User)