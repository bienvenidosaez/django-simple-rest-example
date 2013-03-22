from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

from simple_rest import Resource

from realestate.core.models import VCardRequirement, VCard

import json



class VCardRequirementResource(Resource):
    """
        Represents an VCardRequirement resource.
    """

    def get(self, request, req_id=None, **kwargs):
        """
            Returns the VCard resource that matches the 
            recieved `req_id`.
            Otherwise, returns the list of all VCards.
        """
        json_serializer = serializers.get_serializer('json')()
        if req_id:
            advs = json_serializer.serialize(VCardRequirement.objects.filter(id=req_id))
        else:
            advs = json_serializer.serialize(VCardRequirement.objects.all())
        return HttpResponse(advs, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        data = json.loads(request.body)
        vcard_id = data.get('vcard_id')
        key_feature = data.get('key_feature')
        value_feature = data.get('value_feature')

        try:
            vcard = VCard.objects.get(id=vcard_id)

            # Dont allow users to add vcards of vcard
            # that they don't own.
            if vcard.user == request.user:
                req = VCardRequirement.objects.create(key_feature=key_feature, value_feature=value_feature)
                vcard.requirements.add(req)
                vcard.save()
                return HttpResponse(status=201)
            else:
                return HttpResponse(status=401)
        except Exception, e:
            print e
            return HttpResponse(status=500)
            


    def put(self, request, req_id, *args, **kwargs):
        """
            Updates the model:
            Iterates through the `**kwargs`` and 
            updates the attributes.
        """
        data = json.loads(request.body)
        vcard = VCardRequirement.objects.get(id=req_id)
        for attr, value in data.iteritems():
            setattr(vcard, attr, value)

        vcard.save()
        return HttpResponse(status=200)





    def delete(self, request, req_id):
        # Checks if the user in the request 
        # is the owner of the vcard. If True, removes
        # the VCardRequirement that matches the provided `req_id`.

        user = request.user
        try:
            vcard = VCardRequirement.objects.get(id=req_id)
            if vcard.adv.user == user:
                vcard.delete()
                return HttpResponse(status=200)
            else:
                # Return unauthorized if the request's user
                # isn't the owner of the VCardRequirementResource.
                return HttpResponse(status=401)
        except Exception, e:
            print e
            return HttpResponse(status=500)
