from rest_framework import serializers
from .models import Place, PlaceImage, PlaceHighlight, PlaceOffer


class PlaceImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceImage
        fields = ["id", "image"]


class PlaceHighlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceHighlight
        fields = ["id", "title", "sub_title", "icon"]


class PlaceOfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOffer
        fields = ["id", "name", "icon"]


class PlaceDetailSerializer(serializers.ModelSerializer):
    images = PlaceImageSerializer(many=True, read_only=True)
    highlights = PlaceHighlightSerializer(many=True, read_only=True)
    offers = PlaceOfferSerializer(many=True, read_only=True)

    class Meta:
        model = Place
        fields = [
            "id",
            "title",
            "slug",
            "description",
            "place_type",
            "images",
            "highlights",
            "offers",
        ]
