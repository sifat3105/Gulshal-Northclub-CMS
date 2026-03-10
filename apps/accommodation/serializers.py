from rest_framework import serializers
from .models import (
    AccommodationHero,
    GalleryImage,
    BannerImage,
    Luxury,
    Provide,
    ImpressionsImages,
    Impressions,
    Suite,
    SuiteImage,
)

# Accommodation Hero Serializer
class AccommodationHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationHero
        fields = '__all__'


# Gallery Image Serializer
class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = '__all__'


# Banner Image Serializer
class BannerImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BannerImage
        fields = '__all__'


# Luxury Serializer
class LuxurySerializer(serializers.ModelSerializer):
    class Meta:
        model = Luxury
        fields = '__all__'


# Provide (We Provide Section) Serializer
class ProvideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provide
        fields = '__all__'


# Below Impressions Serializer
class ImpressionsImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImpressionsImages
        fields = '__all__'


# Main Impressions Serializer
class ImpressionsSerializer(serializers.ModelSerializer):
    impressions_image = ImpressionsImagesSerializer(read_only=True)

    class Meta:
        model = Impressions
        fields = '__all__'




#Suite & Suite Image Serializers
class SuiteImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = SuiteImage
        fields = ['id', 'image', 'is_cover', 'order']

    def get_image(self, obj):
        if obj.image:
            return obj.image.url
        return None
        

class SuiteListSerializer(serializers.ModelSerializer):
    cover_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Suite
        fields = ['id', 'title', 'slug', 'area', 'bed_type', 'max_guests', 'description', 'price_per_night', 'cover_image']
        
        
    def get_cover_image(self, obj):
        cover = obj.images.filter(is_cover=True).first() or obj.images.first()
        if cover and cover.image:
            return cover.image.url
        return None
    

class SuiteDetailSerializer(serializers.ModelSerializer):
    images = SuiteImageSerializer(many=True, read_only=True)
    
    class Meta:
        model = Suite
        fields = ['id', 'title', 'slug', 'area', 'bed_type', 'max_guests', 'description', 'price_per_night', 'images']
        


        