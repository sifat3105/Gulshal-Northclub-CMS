from django.db import models


# Event hero model
class EventHero(models.Model):
    EVENT_TYPE_CHOICES = [
        ('running', 'Running Event Hero'),
        ('upcoming', 'Upcoming Event Hero'),
        ('past', 'Past Event Hero'),
    ]

    hero_title = models.CharField(max_length=255)
    hero_description = models.TextField(blank=True, null=True)
    hero_image = models.ImageField(upload_to="events/images/")
    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
        db_index=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.hero_title} ({self.event_type})"


class RunningEventHero(EventHero):
    class Meta:
        proxy = True
        verbose_name = "Running Event Hero"
        verbose_name_plural = "Running Event Heroes"


class UpcomingEventHero(EventHero):
    class Meta:
        proxy = True
        verbose_name = "Upcoming Event Hero"
        verbose_name_plural = "Upcoming Event Heroes"


class PastEventHero(EventHero):
    class Meta:
        proxy = True
        verbose_name = "Past Event Hero"
        verbose_name_plural = "Past Event Heroes"



#  Event section model
class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        # Event Status
        ('running', 'Running Event'),
        ('upcoming', 'Upcoming Event'),
        ('past', 'Past Event'),
        ('past_photo', 'Past Event Photo'),
        ('completed', 'Recently Completed Event'),

        # Experience Sections
        ('fine_dining', 'Fine Dining & Signature Experiences'),
        ('live_music', 'Live Music Shows & Unforgettable Memories'),
        ('fine_dining_2', 'Fine Dining (Second Section)'),

        # Gallery
        ('gallery', 'All Event Photos'),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=50,choices=EVENT_TYPE_CHOICES,db_index=True)
    event_date = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.event_type})"


class EventImage(models.Model):
    event = models.ForeignKey(
        Event, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="events/images/")

    def __str__(self):
        return f"Image of {self.event.title}"

 
# ===== EVENT STATUS (Proxy Models) =====
class RunningEvent(Event):
    class Meta:
        proxy = True
        verbose_name = "Running Event"
        verbose_name_plural = "Running Events"


class UpcomingEvent(Event):
    class Meta:
        proxy = True 
        verbose_name = "Upcoming Event"
        verbose_name_plural = "Upcoming Events"


class PastEvent(Event):
    class Meta:
        proxy = True
        verbose_name = "Past Event"
        verbose_name_plural = "Past Events"


class PastEventPhoto(Event):
    class Meta:
        proxy = True
        verbose_name = "Past Event Photo"
        verbose_name_plural = "Past Event Photos"


class CompletedEvent(Event):
    class Meta:
        proxy = True
        verbose_name = "Recently Completed Event"
        verbose_name_plural = "Recently Completed Events"


# ===== EXPERIENCE SECTIONS =====
class FineDining(Event):
    class Meta:
        proxy = True
        verbose_name = "Fine Dining & Signature Experiences"
        verbose_name_plural = "Fine Dining Experiences"


class LiveMusic(Event):
    class Meta:
        proxy = True
        verbose_name = "Live Music Shows & Memories"
        verbose_name_plural = "Live Music Shows"


class FineDiningSecond(Event):
    class Meta:
        proxy = True
        verbose_name = "Fine Dining (Second Section)"
        verbose_name_plural = "Fine Dining (Second Section)"


# ===== GALLERY =====
class EventGallery(Event):
    class Meta:
        proxy = True
        verbose_name = "All Event Photos"
        verbose_name_plural = "All Event Photos"
