from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from simple_rest import Resource

from realestate.core.models import Adv

import json


class AdvResource(Resource):
    """
        Represents an Adv resource.
    """

    def get(self, request, adv_id=None, **kwargs):
        """
            Returns the adv resource that matches the 
            recieved `adv_id`.
            Otherwise, returns the list of all advs.
        """
        json_serializer = serializers.get_serializer('json')()
        if adv_id:
            advs = json_serializer.serialize(Adv.objects.filter(id=adv_id))
        else:
            advs = json_serializer.serialize(Adv.objects.all())
        return HttpResponse(advs, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        data = json.loads(request.body)
        user = request.user
        adv_type = data.get('type')
        price = data.get('price')

        Adv.objects.create(user=user, type=adv_type, price=price, date=timezone.now())

        return HttpResponse(status=201)

    def put(self, request, adv_id,*args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """

        data =  request.PUT.dict()
        adv = Adv.objects.get(id=adv_id)
        for attr, value in data.iteritems():
            print value
            setattr(adv, attr, value)

        adv.save()
        return HttpResponse(status=200)
        

    def delete(self, request, adv_id):
        # Checks if the user in the request 
        # is the owner of the adv. If True, removes
        # the Adv that matches the provided `adv_id`.

        user = request.user
        adv = Adv.objects.get(id=adv_id)
        if adv.user == user:
            adv.delete()
        return HttpResponse(status=200)

