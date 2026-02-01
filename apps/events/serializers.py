from rest_framework import serializers
from .models import EventHero, Event, EventImage

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
