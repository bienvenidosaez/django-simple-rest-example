from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from simple_rest import Resource

from realestate.core.models import Object, Adv

import json



@csrf_exempt
def search(request):
    """
        Returns vcards that match the criteria (key/value pairs) 
        sent in JSON format. 
    """
    json_serializer = serializers.get_serializer('json')()
    data = json.loads(request.body)
    response = []
    for key, value in data.iteritems():
        response += Object.objects.filter(key_feature=key, value_feature=value)

    response = json_serializer.serialize(response)
    return HttpResponse(response, content_type="application/json", status=200)




class VCardResource(Resource):
    """
        Represents an Object resource.
    """

    def get(self, request, vcard_id=None, **kwargs):
        """
            Returns the VCard resource that matches the 
            recieved `vcard_id`.
            Otherwise, returns the list of all VCards.
        """
        json_serializer = serializers.get_serializer('json')()
        if vcard_id:
            advs = json_serializer.serialize(Object.objects.filter(id=vcard_id))
        else:
            advs = json_serializer.serialize(Object.objects.all())
        return HttpResponse(advs, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        data = json.loads(request.body)
        adv_id = data.get('adv_id')
        key_feature = data.get('key_feature')
        value_feature = data.get('value_feature')

        try:
            adv = Adv.objects.get(id=adv_id)

            # Dont allow users to add vcards of adv
            # that they don't own.
            if adv.user == request.user:
                Object.objects.create(adv=adv, key_feature=key_feature, value_feature=value_feature)
                return HttpResponse(status=201)
            else:
                return HttpResponse(status=401)
        except Exception, e:
            print e
            return HttpResponse(status=500)
            


    def put(self, request, vcard_id, *args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """
        data = request.PUT.dict()
        vcard = Object.objects.get(id=vcard_id)
        for attr, value in data.iteritems():
            setattr(vcard, attr, value)

        vcard.save()
        return HttpResponse(status=200)





    def delete(self, request, vcard_id):
        # Checks if the user in the request 
        # is the owner of the vcard. If True, removes
        # the Object that matches the provided `vcard_id`.

        user = request.user
        try:
            vcard = Object.objects.get(id=vcard_id)
            if vcard.adv.user == user:
                vcard.delete()
                return HttpResponse(status=200)
            else:
                # Return unauthorized if the request's user
                # isn't the owner of the VCardResource.
                return HttpResponse(status=401)
        except Exception, e:
            print e
            return HttpResponse(status=500)
