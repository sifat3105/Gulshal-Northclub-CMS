from django.db import models

# About Section
class AboutHero(models.Model):
    hero_image = models.ImageField(upload_to='About/about_us')
    
    def __str__(self):
        return self.hero_image.name
    

class Topgallery(models.Model):
    top_image = models.ImageField(upload_to='About/gallery')
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Top Gallery"
        verbose_name_plural = "Top Gallery"
    

class Bottomgallery(models.Model):
    bottom_image = models.ImageField(upload_to='About/gallery')
    title = models.CharField(max_length=255)
    sub_title = models.TextField()
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bottom Gallery"
        verbose_name_plural = "Bottom Gallery"
    

class AboutForHeritage(models.Model):
    image = models.ImageField(upload_to='About/gallery')
    title = models.CharField(max_length=255)
    descriptions = models.TextField()
    
    def __str__(self):
        return self.title


class President(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='about/president')
    designation = models.CharField(max_length=150)
    message = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name


class PresidentSocialMediaLink(models.Model):
    president = models.ForeignKey(President,on_delete=models.CASCADE,related_name='social_links')
    platform_name = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return f"{self.platform_name} - {self.president.name}"

# Member Section
class MemberType(models.Model):
    TYPE_CHOICES = [
        ("board_of_director", "Board of Directors"),
        ("executive_member", "Executive Member"),
        ("founder_member", "Founder Member"),
    ]

    type_name = models.CharField(max_length=50, choices=TYPE_CHOICES, unique=True)

    def __str__(self):
        return self.get_type_name_display()


class BoardMember(models.Model):
    member_image = models.ImageField(upload_to="About/board_members/")
    member_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=150)
    member_type = models.ForeignKey(MemberType, on_delete=models.CASCADE, related_name="members")
    detail_title = models.CharField(max_length=150, blank=True, null=True)
    detail_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.member_name} ({self.designation})"


class DetailImage(models.Model):
    board_member = models.ForeignKey(BoardMember, on_delete=models.CASCADE, related_name="detail_images")
    detail_image = models.ImageField(upload_to="About/board_members/details/", blank=True, null=True)

    def __str__(self):
        return self.detail_image.name


# ── Club History Section ──────────────────────────────────────────────────────
class ClubHistory(models.Model):
    SECTION_CHOICES = [
        ("beyond_thinking",       "Beyond Thinking"),
        ("beyond_thinking_left",  "Beyond Thinking Left"),
        ("beyond_thinking_right", "Beyond Thinking Right"),
    ]

    section_type = models.CharField(
        max_length=30,
        choices=SECTION_CHOICES,
        db_index=True,
    )
    title       = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return f"{self.get_section_type_display()} — {self.title}"

    class Meta:
        verbose_name        = "Club History"
        verbose_name_plural = "Club History"


class ClubHistoryImage(models.Model):
    club_history = models.ForeignKey(
        ClubHistory, on_delete=models.CASCADE, related_name="images"
    )
    image = models.ImageField(upload_to="about/club_history/")

    def __str__(self):
        return f"Image for {self.club_history}"

    class Meta:
        verbose_name        = "Club History Image"
        verbose_name_plural = "Club History Images"


# Proxy models for clean admin separation
class BeyondThinking(ClubHistory):
    class Meta:
        proxy = True
        verbose_name        = "Beyond Thinking"
        verbose_name_plural = "Beyond Thinking"


class BeyondThinkingLeft(ClubHistory):
    class Meta:
        proxy = True
        verbose_name        = "Beyond Thinking Left"
        verbose_name_plural = "Beyond Thinking Left"


class BeyondThinkingRight(ClubHistory):
    class Meta:
        proxy = True
        verbose_name        = "Beyond Thinking Right"
        verbose_name_plural = "Beyond Thinking Right"


class SocialMediaLink(models.Model):
    board_member = models.ForeignKey(BoardMember, on_delete=models.CASCADE, related_name="social_links")
    platform_name = models.CharField(max_length=50, help_text="e.g. Facebook, Twitter")
    url = models.URLField()

    def __str__(self):
        return f"{self.platform_name} for {self.board_member.member_name}"
