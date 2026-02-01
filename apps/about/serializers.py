from rest_framework import serializers
from .models import *

class AboutHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutHero
        fields = '__all__'

class TopgallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Topgallery
        fields = '__all__'

class BottomgallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Bottomgallery
        fields = '__all__'

class AboutForHeritageSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutForHeritage
        fields = '__all__'


class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PresidentSocialMediaLink
        fields = ['platform_name', 'url']


class AboutPresidentSerializer(serializers.ModelSerializer):
    social_links = SocialMediaLinkSerializer(many=True, read_only=True)

    class Meta:
        model = President
        fields = [
            'id',
            'name',
            'designation',
            'email',
            'message',
            'image',
            'social_links',
        ]


class MemberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        fields = '__all__'

class DetailImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailImage
        fields = '__all__'

class SocialMediaLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaLink
        fields = '__all__'

class BoardMemberSerializer(serializers.ModelSerializer):
    social_links = SocialMediaLinkSerializer(many=True, read_only=True)
    detail_images = DetailImageSerializer(many=True, read_only=True)
    member_type = MemberTypeSerializer(read_only=True)

    class Meta:
        model = BoardMember
        fields = '__all__'
