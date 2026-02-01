from django.forms import fields
from rest_framework import serializers
from .models import  NoticeCard 

class NoticeCardSerializers(serializers.ModelSerializer):
    class Meta :
        model =  NoticeCard
        fields = '__all__'

