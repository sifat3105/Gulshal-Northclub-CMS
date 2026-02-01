from django.db import models

# Base Model for timestamps 
class TimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True 


# Hero Section
class Hero(TimeStamp, models.Model):
    bg_image = models.ImageField(upload_to='home/hero')
    title = models.CharField(max_length=255)
    sub_title = models.TextField()

    def __str__(self):
        return self.title


# Club Facilities Section Head
class ClubFacilitiesHead(TimeStamp, models.Model):
    head_text = models.CharField(max_length=255, default="Exclusive Club Facilities")

    def __str__(self):
        return self.head_text


# Club Facilities Items
class Facilities(TimeStamp, models.Model):
    image = models.ImageField(upload_to='home/facilities')
    title = models.CharField(max_length=255)
    designation = models.TextField()

    def __str__(self):
        return self.title


# Our Moments Section Head
class OurMomentsHead(TimeStamp, models.Model):
    head_text = models.CharField(max_length=255, default="Our Moments")
    sub_head = models.CharField(max_length=255, default="Our Special Moments")

    def __str__(self):
        return self.head_text


# Our Moments Images
class OurMoments(TimeStamp, models.Model):
    our_moment = models.ForeignKey(OurMomentsHead, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='home/moments')

    def __str__(self):
        return f"Moment - {self.our_moment.head_text}"


# Affiliations & Collaborations Section Head
class AffiliatCollabHead(TimeStamp, models.Model):
    head_text = models.CharField(max_length=255, default="Affiliations & Collaborations")
    sub_head = models.CharField(max_length=255, default="Our Partnerships")

    def __str__(self):
        return self.head_text


# Affiliations & Collaborations Logos
class AffiliatCollab(TimeStamp, models.Model):
    logo = models.ImageField(upload_to='home/affiliations')

    def __str__(self):
        return "Affiliation Logo"


# Club Events Section Head
class ClubEventHead(TimeStamp, models.Model):
    head_text = models.CharField(max_length=255, default="Our Club Events")

    def __str__(self):
        return self.head_text


# Club Events Items
class ClubEvents(TimeStamp, models.Model):
    images = models.ImageField(upload_to='home/club', null=True, blank=True)
    event_name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.event_name
