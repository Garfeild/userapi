from django.contrib.auth.models import User
from django.db.utils import IntegrityError
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from decorators import basic_auth_required

import json


class UserView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserView, self).dispatch(*args, **kwargs)

    @basic_auth_required
    def get(self, request, pk):
        # Returns a single user object.
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            return HttpResponse('User not found', status=404)

        response = {'id': user.pk, 'username': user.username}
        return HttpResponse(json.dumps(response, indent=4))


class UserListView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super(UserListView, self).dispatch(*args, **kwargs)

    @basic_auth_required
    def get(self, request):
        # Returns a list of all users.
        users = [{'id': u.pk, 'username': u.username}
            for u in User.objects.all()]
        return HttpResponse(json.dumps(users, indent=4))

    def post(self, request):
        # Handles registration of a new user.
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        user = User(username=username)
        user.set_password(password)

        try:
            user.save()
        except IntegrityError:
            return HttpResponse('Username exists\n', status=409)

        return HttpResponse(json.dumps({'id': user.pk}, indent=4), status=201)
