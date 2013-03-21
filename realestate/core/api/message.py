from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from simple_rest import Resource

from realestate.core.models import Message, User, Adv

import json
from datetime import datetime


class MessageResource(Resource):
    """
        Represents a Message Resource.
    """
    
    def get(self, request, message_id=None, **kwargs):
        """
            Returns one message that matches message_id (if
            provided) of the auth'ed user.
            Returns all the messages of the auth'ed user (if
            message_id isn't provided).
        """
        user = request.user
        json_serializer = serializers.get_serializer('json')()
        if message_id:
            messages = json_serializer.serialize(Message.objects.filter(
                                         id=message_id,
                                         user_ins=user.pk))
        else:
            messages = json_serializer.serialize(Message.objects.filter(user_ins=user.pk))
        return HttpResponse(messages, content_type="application/json", status=200)

 


    def post(self, request,*args,**kwargs):
        """
            Sends a new message where `user_reads` is
            the auth'ed user.
        """

        data = json.loads(request.body)
        user_reads = request.user
        adv_id = data.get('adv_id')
        user_ins_id = data.get('user_id')
        message_text = data.get('message_text')
        try:
            user_ins = User.objects.get(id=user_ins_id)
            adv = Adv.objects.get(id=adv_id, user=user_ins)
            message = Message.objects.create(
                adv = adv,
                user_read = user_reads,
                user_ins = user_ins,
                date = datetime.now(),
                message = message_text,
                )
            
            return HttpResponse(status=200)
        except Exception, e:
            print e
            return HttpResponse(status=500)














    







 
