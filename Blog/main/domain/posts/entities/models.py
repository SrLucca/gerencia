from django.db import models
# Create your models here.
from django.db import models
from main.domain.users.entities.models import User
import uuid

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=250)
    created_at = models.TimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
