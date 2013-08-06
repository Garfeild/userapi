from django.contrib.auth import login, authenticate
from django.http import HttpResponse

import base64


def basic_auth_required(func):
    def wrapper(self, request, *args, **kwargs):
        # Check whether Authorization is available.
        user = None
        auth = request.META.get('HTTP_AUTHORIZATION')
        if auth:
            try:
                username, password = base64.b64decode(auth.split(' ')[1]).decode('ascii').split(':')
            except:
                # Invalid Authorization header
                return HttpResponse(status=400)
            print(username, password)
            user = authenticate(username=username, password=password)
        if user is None:
            response = HttpResponse('Authorization required', status=401)
            response['WWW-Authenticate'] = 'Basic realm="User API"'
            return response
        else:
            return func(self, request, *args, **kwargs)
    return wrapper
