from django.db import models
from django.utils.text import slugify

# Create your models here.

# Base Model for timestamps (OPTIONAL but recommended)
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 

#  Accommodation Hero Section Model
class AccommodationHero(TimeStamp):
    bg_image = models.ImageField(upload_to='accommodation/hero', blank=True, null=True)
    title = models.CharField(max_length=255)
    sub_title = models.TextField()

    def __str__(self):
        # Return title instead of image object for better readability
        return self.title


#  Top Gallery Image Model
class GalleryImage(TimeStamp):
    top_image = models.ImageField(upload_to='accommodation/gallery', blank=True, null=True)
    below_image = models.ImageField(upload_to='accommodation/gallery', blank=True, null=True)
    title = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self):
        return self.title


#  Banner Image Model
class BannerImage(TimeStamp):
    banner_image = models.ImageField(upload_to='accommodation/banner', blank=True, null=True)
    title = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self):
        return self.title


#  Luxury Section Model
class Luxury(TimeStamp):
    image = models.ImageField(upload_to='accommodation/gallery')
    title = models.CharField(max_length=255)
    descriptions = models.TextField()

    def __str__(self):
        return self.title


#  We Provide Section Model
class Provide(TimeStamp):
    service_icon = models.ImageField(upload_to='accommodation/provide', blank=True, null=True)
    service_name = models.CharField(max_length=255)
    short_descriptions = models.TextField()

    def __str__(self):
        return self.service_name


# Authenticated Impressions Section

class Impressions(TimeStamp):
    """Main section: logo + title (center part)"""
    logo = models.ImageField(upload_to='accommodation/impressions/logo/', blank=True,null=True)
    title = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title if self.title else "Impression Section"


class ImpressionsImages(TimeStamp):
    """Multiple images for left/right collage"""
    impression = models.ForeignKey(
        Impressions,
        related_name='images',
        on_delete=models.CASCADE
    )
    image = models.ImageField(
        upload_to='accommodation/impressions/images/',
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Image for {self.impression.title}"
    
    

class Suite(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique = True)
    area = models.PositiveIntegerField(help_text= "Area in m²")
    bed_type = models.CharField(max_length=255)
    max_guests = models.PositiveIntegerField()
    description = models.TextField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    is_active = models.BooleanField(default=True)
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['order', 'created_at']
        
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)



class SuiteImage(models.Model):
    suite = models.ForeignKey(Suite, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='accommodation/suites/')
    is_cover = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return f"{self.suite.title} Image {self.order}"