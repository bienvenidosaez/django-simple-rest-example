from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource

from realestate.core.models import User

class UserResource(Resource):
    """
        Represents a User resource.
        
    """

    def get(self, request, username=None, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        if username:
            users = json_serializer.serialize(User.objects.filter(username=username))
        else:
            users = json_serializer.serialize(User.objects.all())
        return HttpResponse(users, content_type='application/json', status=200)

    

    def delete(self, request, username):
        user = User.objects.get(username=username)
        user.delete()
        return HttpResponse(status=200)

