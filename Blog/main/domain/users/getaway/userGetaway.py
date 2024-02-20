from users.entities.models import User

class UserGateway:
    def save(self, user):
        user.save()

    def find(self, id):
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None

    def list(self):
        return User.objects.all()