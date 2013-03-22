from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource

from realestate.core.models import User

class UserResource(Resource):
    """
        Represents a User resource.
    """

    def get(self, request, username=None, **kwargs):
        """
            Returns the user resource that matches the 
            recieved `username`.
            Otherwise, returns the list of all users.
        """

        json_serializer = serializers.get_serializer('json')()
        if username:
            users = json_serializer.serialize(User.objects.filter(username=username))
        else:
            users = json_serializer.serialize(User.objects.all())
        return HttpResponse(users, content_type='application/json', status=200)

    
    def put(self, request, username,*args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """
        data = json.loads(request.body)
        user = User.objects.get(username=username)
        for attr, value in data.iteritems():
            setattr(user, attr, value)

        user.save()

        return HttpResponse(status=200)




    def delete(self, request, username):
        """
            Deletes the user that matches `username`.
        """
        user = User.objects.get(username=username)
        user.delete()
        return HttpResponse(status=200)

