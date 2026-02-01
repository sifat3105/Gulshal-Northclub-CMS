from django.db import models

# Create your models here.

# Logo & Short Description
class FooterBrand(models.Model):
    baground_image = models.ImageField(upload_to='Footer/bg_image')
    logo = models.ImageField(upload_to="footer/logo")
    short_text = models.TextField()

    def __str__(self):
        return "Footer Brand Section"


# Useful Links
class UsefulLink(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title


# Social Media
class SocialMedia(models.Model):
    name = models.CharField(max_length=100)
    icon = models.FileField(upload_to='Footer/social-icon')
    url = models.URLField()

    def __str__(self):
        return self.name


# Contact Information
class ContactInfo(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    office_phone = models.CharField(max_length=20)

    def __str__(self):
        return "Contact Information"


# Footer Copyright
class FooterCopyright(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text
