from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from simple_rest import Resource

from realestate.core.models import Adv, Object

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
            advs = serializers.serialize("json", Adv.objects.filter(id=adv_id), relations=('obj',))
        else:
            advs = serializers.serialize("json", Adv.objects.all(), relations=('obj',))
        return HttpResponse(advs, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        data = json.loads(request.body)
        print data.get('obj')
        user = request.user
        adv_type = data.get('type')
        price = data.get('price')

        adv = Adv.objects.create(user=user, type=adv_type, price=price, date=timezone.now())
        for o in data.get('obj'):
            obj = Object.objects.create(
                key_feature=o.get('key_feature'),
                value_feature= o.get('value_feature')
                )

            adv.obj.add(obj)
            adv.save()
        return HttpResponse(status=201)

    def put(self, request, adv_id,*args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """
        data = json.loads(request.body)
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

