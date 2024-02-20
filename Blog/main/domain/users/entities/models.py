from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.CharField(max_length=255, blank=False, null=False)
    created_at = models.TimeField(auto_now=True, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    @classmethod
    def create(cls, name):
        return cls.objects.create(name=name)

    def validate(self):
        if not self.id:
            raise DomainException("User id is required")

        if not self.name:
            raise DomainException("User name is required")

    def add_user(self, user):
        self.users.add(user)

    def remove_user(self, user):
        self.user.remove(user)

class DomainException(Exception):
    pass
