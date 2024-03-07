from main.domain.users.entities.models import User
from main.domain.users.serializer.serializers import UserSerializer

import uuid

class UserGateway:
    def save(self, user_data):
        if user_data.is_valid():
            user_data.save()
            return {'data': user_data.data, 'status': 201}
        else:
            return {'errors': 'Missing required data', 'status': 400}