from django.db import models

# Create your models here.


class ContactPageImage(models.Model):
    contact_baground = models.ImageField(upload_to='contact/baground')
    def __str__(self):
        return self.contact_baground.name


class Appointment(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
