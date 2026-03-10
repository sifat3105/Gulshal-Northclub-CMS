from rest_framework import serializers
from .models import EventHero, Event, EventImage, RunningEventSlider, LiveMusicImage, LiveMusic

# Event Hero serializers section
class EventHeroSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventHero
        fields = [
            "id",
            "hero_title",
            "hero_description",
            "hero_image",
            "event_type",
        ]



# Event serializers section
class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImage
        fields = ["id", "image"]


class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = [
            "id",
            "title",
            "description",
            "event_type",
            "event_date",
            "is_active",
            "images",
            "created_at",
        ]


# ── Running Event Slider Serializer ───────────────────────────────────────────
class RunningEventSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model  = RunningEventSlider
        fields = ["id", "image", "order"]


class LiveMusicImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LiveMusicImage
        fields = ['id', 'image']

class LiveMusicSerializer(serializers.ModelSerializer):
    gallery_1 = serializers.SerializerMethodField()
    gallery_2 = serializers.SerializerMethodField()
    gallery_3 = serializers.SerializerMethodField()

    class Meta:
        model = LiveMusic
        fields = ['id', 'title', 'description', 'gallery_1', 'gallery_2', 'gallery_3']

    def get_gallery_1(self, obj):
        images = obj.live_music_images.filter(image_type='gallery_1')
        return LiveMusicImageSerializer(images, many=True, context=self.context).data

    def get_gallery_2(self, obj):
        images = obj.live_music_images.filter(image_type='gallery_2')
        return LiveMusicImageSerializer(images, many=True, context=self.context).data

    def get_gallery_3(self, obj):
        images = obj.live_music_images.filter(image_type='gallery_3')
        return LiveMusicImageSerializer(images, many=True, context=self.context).data
