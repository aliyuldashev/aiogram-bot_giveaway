from django.shortcuts import render, HttpResponse
from .models import Users,Channel,Give,Admins,Asosiy
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class give_product(serializers.ModelSerializer):
    class Meta:
        model = Give
        fields = '__all__'

class give_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Give.objects.all()
        serlized_agent = give_product(all_agent, many=True)
        return Response(serlized_agent.data)

class users_product(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'

class users_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Users.objects.all()
        serlized_agent = users_product(all_agent, many=True)
        return Response(serlized_agent.data)

class channel_product(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'

class channel_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Channel.objects.filter(id = kwargs['pk'])
        serlized_agent = channel_product(all_agent, many=True)
        return Response(serlized_agent.data)


class admins_product(serializers.ModelSerializer):
    class Meta:
        model = Admins
        fields = '__all__'

class admins_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Admins.objects.all()
        serlized_agent = admins_product(all_agent, many=True)
        return Response(serlized_agent.data)

class asosiy_product(serializers.ModelSerializer):
    class Meta:
        model = Asosiy
        fields = '__all__'

class asosiy_view(APIView):
    def get(self,*args,**kwargs):
        all_agent = Asosiy.objects.all()
        serlized_agent = asosiy_product(all_agent, many=True)
        return Response(serlized_agent.data)


def channel_post(request,telegram_id,username,title):
    cre, get = Channel.objects.get_or_create(telegram_id=telegram_id,username=username,title=title)
    cre.save()
    return HttpResponse('{"nothing":1}')

def channel_edit(request,telegram_id1):
    try:
        get = Channel.objects.get(telegram_id = telegram_id1)
        get.delete()
        get.save()
        return HttpResponse('{"nothing":1}')
    except:
        return HttpResponse('{"nothing":0}')

def give_post(request,give,channel_ids,admin):
    give,get = Give.objects.get_or_create(name=give,admin=admin)
    channel = Channel.objects.get(telegram_id=channel_ids)
    give.channel.add(channel)
    give.save()
    return HttpResponse('{"nothing":1}')
def give_time(request,give,time,admin):
    give = Give.objects.get(name=give,admin=admin)
    give.time = f'{time}'
    give.save()
    return HttpResponse('{"nothing":1}')

def user_add_to_give(requets,telegram_id,username,name,give):
    user, get = Users.objects.get_or_create(telegram_id=telegram_id,username=username,name=name)
    give =Give.objects.get(id=give)
    give.users.add(user)
    give.save()
    user.save()
    return HttpResponse('{"nothing":1}')

