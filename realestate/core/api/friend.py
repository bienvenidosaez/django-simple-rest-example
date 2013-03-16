from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from simple_rest import Resource

from realestate.core.models import FriendList, User

import json
class FriendResource(Resource):
    """
        Represents an FriendList resource.
    """

    def get(self, request, friend_id=None, **kwargs):
        """
            Returns the friend resource that matches the 
            recieved `friend_id`.
            Otherwise, returns the list of all friends.
        """
        json_serializer = serializers.get_serializer('json')()
        if friend_id:
            friends = json_serializer.serialize(FriendList.objects.filter(id=friend_id))
        else:
            friends = json_serializer.serialize(FriendList.objects.all())
        return HttpResponse(friends, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        
        data = json.loads(request.body)

        user = request.user
        key_feature = data.get('key_feature')
        value_feature = data.get('value_feature')
        social = data.get('social')

        FriendList.objects.create(
                id_user = user.id,
                key_feature = key_feature,
                value_feature = value_feature,
                social = social
            )

        return HttpResponse(status=201)

    def put(self, request, friend_id,*args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """

        data =  request.PUT.dict()
        friend = FriendList.objects.get(id=friend_id)
        for attr, value in data.iteritems():
            print value
            setattr(friend, attr, value)

        friend.save()
        return HttpResponse(status=200)
        

    def delete(self, request, friend_id):
        # Checks if the user in the request 
        # is the owner of the friend. If True, removes
        # the FriendList that matches the provided `friend_id`.

        user = request.user
        friend = FriendList.objects.get(id=friend_id)
        if friend.user == user:
            friend.delete()
        return HttpResponse(status=200)

