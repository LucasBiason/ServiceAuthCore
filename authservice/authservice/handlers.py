import datetime
from rest_framework_jwt.settings import api_settings


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'exp':datetime.datetime.utcnow() + api_settings.JWT_EXPIRATION_DELTA 
        #'user': UserSerializer(user, context={'request': request}).data
    }