from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource

from realestate.core.models import Object, Adv

class VCardResource(Resource):
    """
        Represents an Object resource.
        
    """

    def get(self, request, vcard_id=None, **kwargs):

        json_serializer = serializers.get_serializer('json')()
        if vcard_id:
            advs = json_serializer.serialize(Object.objects.filter(id=vcard_id))
        else:
            advs = json_serializer.serialize(Object.objects.all())
        return HttpResponse(advs, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        # Uses request.user to prevent creating
        # resources on behalf of other users.
        
        adv_id = request.POST.get('advID')
        key_feature = request.POST.get('keyFeature')
        value_feature = request.POST.get('valueFeature')

        try:
            adv = Adv.objects.get(id=adv_id)
            Object.objects.create(adv=adv, key_feature=key_feature, value_feature=value_feature)
            return HttpResponse(status=201)
        except Exception, e:
            print e
            return HttpResponse(status=500)
            

    def delete(self, request, vcard_id):
        # Checks if the user in the request 
        # is the owner of the adv. If True, removes
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
