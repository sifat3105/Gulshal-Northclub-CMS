from django.db import models


class Place(models.Model):
    PLACE_TYPE_CHOICES = [
        ('healthcare_gym', 'Healthcare & Gym'),
        ('salon', 'Salon'),
        ('lounges_party', 'Lounges Party'),
        ('swimming_pool', 'Swimming Pool'),
        ('billiard_smoking', 'Billiard & Smoking'),
        ('library', 'Library'),
        ('beauty_parlor', 'Beauty Parlor'),
        ('laundry', 'Laundry'),
        ('card_room', 'Card Room'),
        ('banquet_hall', 'Banquet Hall'),
    ]

    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    place_type = models.CharField(max_length=50, choices=PLACE_TYPE_CHOICES)

    def __str__(self):
        return f"{self.title} ({self.place_type})"


class PlaceImage(models.Model):
    place = models.ForeignKey(
        Place, related_name="images", on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="places/images/")

    def __str__(self):
        return f"Image of {self.place.title}"


class PlaceHighlight(models.Model):
    place = models.ForeignKey(
        Place, related_name="highlights", on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    icon = models.ImageField(
        upload_to="places/highlights/", blank=True, null=True
    )

    def __str__(self):
        return self.title


class PlaceOffer(models.Model):
    place = models.ForeignKey(
        Place, related_name="offers", on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    icon = models.ImageField(
        upload_to="places/offers/", blank=True, null=True
    )

    def __str__(self):
        return self.name

# PROXY MODELS (Admin separation only)
class healthcare_gym(Place):
    class Meta:
        proxy = True
        verbose_name = "healthcare_gym"
        verbose_name_plural = "healthcare_gym"

class salon(Place):
    class Meta:
        proxy = True
        verbose_name = "salon"
        verbose_name_plural = "salon"

class LoungesParty(Place):
    class Meta:
        proxy = True
        verbose_name = "Lounges Party"
        verbose_name_plural = "Lounges Party"

class SwimmingPool(Place):
    class Meta:
        proxy = True
        verbose_name = "Swimming Pool"
        verbose_name_plural = "Swimming Pool"


class BilliardSmoking(Place):
    class Meta:
        proxy = True
        verbose_name = "Billiard & Smoking"
        verbose_name_plural = "Billiard & Smoking"


class Library(Place):
    class Meta:
        proxy = True
        verbose_name = "Library"
        verbose_name_plural = "Libraries"


class BeautyParlor(Place):
    class Meta:
        proxy = True
        verbose_name = "Beauty Parlor"
        verbose_name_plural = "Beauty Parlors"


class Laundry(Place):
    class Meta:
        proxy = True
        verbose_name = "Laundry"
        verbose_name_plural = "Laundry"


class CardRoom(Place):
    class Meta:
        proxy = True
        verbose_name = "Card Room"
        verbose_name_plural = "Card Rooms"


class BanquetHall(Place):
    class Meta:
        proxy = True
        verbose_name = "Banquet Hall"
        verbose_name_plural = "Banquet Halls"
