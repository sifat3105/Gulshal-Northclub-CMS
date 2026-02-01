from rest_framework import serializers
from .models import (
    Hero,ClubFacilitiesHead,
    Facilities,OurMomentsHead,OurMoments,
    AffiliatCollabHead,AffiliatCollab,
    ClubEventHead,ClubEvents
)


class HeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hero
        fields = '__all__'


class ClubFacilitiesHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubFacilitiesHead
        fields = '__all__'


class FacilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Facilities
        fields = '__all__'


class OurMomentsHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMomentsHead
        fields = '__all__'


class OurMomentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OurMoments
        fields = '__all__'


class AffiliatCollabHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliatCollabHead
        fields = '__all__'


class AffiliatCollabSerializer(serializers.ModelSerializer):
    class Meta:
        model = AffiliatCollab
        fields = '__all__'


class ClubEventHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEventHead
        fields = '__all__'


class ClubEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClubEvents
        fields = '__all__'
