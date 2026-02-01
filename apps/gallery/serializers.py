from rest_framework import serializers
from .models import Gallery, GalleryImage ,GallerySection,GallerySectionImage


class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ["id", "image"]


class GallerySerializer(serializers.ModelSerializer):
    images = GalleryImageSerializer(many=True, read_only=True)

    class Meta:
        model = Gallery
        fields = [
            "id",
            "title",
            "gallery_type",
            "images",
        ]


class GallerySectionImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GallerySectionImage
        fields = ["id", "image"]


class GallerySectionSerializer(serializers.ModelSerializer):
    images = GallerySectionImageSerializer(many=True, read_only=True)

    class Meta:
        model = GallerySection
        fields = [
            "id",
            "page",
            "section_type",
            "title",
            "images",
        ]
