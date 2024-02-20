from django.db import models
from shared.entities import entity
# Create your models here.
from django.db import models
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    author = models.ForeignKey('User')
    content = models.TextField()
    created_at = models.TimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, title):
        return cls.objects.create(title=title)

    def validate(self):
        if not self.id:
            raise DomainException("Post id is required")

        if not self.title:
            raise DomainException("Post title is required")

    def add_post(self, post):
        self.posts.add(post)

    def remove_post(self, post):
        self.posts.remove(post)

class DomainException(Exception):
    pass
