from rest_framework import serializers
from .models import (
    FooterBrand,
    UsefulLink,
    SocialMedia,
    ContactInfo,
    FooterCopyright
)


class FooterBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterBrand
        fields = "__all__"


class UsefulLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsefulLink
        fields = "__all__"


class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = "__all__"


class ContactInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactInfo
        fields = "__all__"


class FooterCopyrightSerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterCopyright
        fields = "__all__"
