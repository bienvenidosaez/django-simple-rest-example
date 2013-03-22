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

    
    def put(self, request, *args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """
        data = json.loads(request.body)
        user = request.user
        for attr, value in data.iteritems():
            setattr(user, attr, value)

        user.save()

        return HttpResponse(status=200)




    def delete(self, request):
        """
            Deletes the user that matches `username`.
        """
        
        request.user.delete()
        return HttpResponse(status=200)

