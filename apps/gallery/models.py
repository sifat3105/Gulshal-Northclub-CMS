from django.db import models


class Gallery(models.Model):
    GALLERY_TYPE_CHOICES = [
        ('memberships', 'Memberships'),
        ('reservation', 'Reservation'),
        ('menu', 'Menu'),
    ]

    title = models.CharField(max_length=255, blank=True, null=True)

    gallery_type = models.CharField(
        max_length=50,
        choices=GALLERY_TYPE_CHOICES,
        db_index=True
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.gallery_type


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="gallery/images/")

    def __str__(self):
        return f"Image of {self.gallery.gallery_type}"


# ===== PROXY MODELS (ADMIN ONLY) =====
class MembershipGallery(Gallery):
    class Meta:
        proxy = True
        verbose_name = "Membership Gallery"
        verbose_name_plural = "Membership Gallery"


class ReservationGallery(Gallery):
    class Meta:
        proxy = True
        verbose_name = "Reservation Gallery"
        verbose_name_plural = "Reservation Gallery"


class MenuGallery(Gallery):
    class Meta:
        proxy = True
        verbose_name = "Menu Gallery"
        verbose_name_plural = "Menu Gallery"



class GallerySection(models.Model):
    PAGE_CHOICES = [
        ('memberships', 'Memberships'),
        ('reservation', 'Reservation'),
        ('menu', 'Menu'),
    ]

    SECTION_CHOICES = [
        ('fine_dining', 'Fine Dining & Signature Experiences'),
        ('live_music', 'Live Music Shows & Unforgettable Memories'),
        ('fine_dining_2', 'Fine Dining & Signature Experiences (Second)'),
    ]

    page = models.CharField(
        max_length=30,
        choices=PAGE_CHOICES,
        db_index=True
    )

    section_type = models.CharField(
        max_length=50,
        choices=SECTION_CHOICES,
        db_index=True
    )

    title = models.CharField(max_length=255, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.page} - {self.section_type}"


class GallerySectionImage(models.Model):
    section = models.ForeignKey(
        GallerySection,
        related_name="images",
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to="experience/images/")

    def __str__(self):
        return f"Image - {self.section}"


# ===== MEMBERSHIPS =====
class MembershipFineDining(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Memberships - Fine Dining"


class MembershipLiveMusic(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Memberships - Live Music"


class MembershipFineDiningSecond(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Memberships - Fine Dining (Second)"


# ===== RESERVATION =====
class ReservationFineDining(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Reservation - Fine Dining"


class ReservationLiveMusic(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Reservation - Live Music"


class ReservationFineDiningSecond(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Reservation - Fine Dining (Second)"


# ===== MENU =====
class MenuFineDining(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Menu - Fine Dining"


class MenuLiveMusic(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Menu - Live Music"


class MenuFineDiningSecond(GallerySection):
    class Meta:
        proxy = True
        verbose_name = "Menu - Fine Dining (Second)"
