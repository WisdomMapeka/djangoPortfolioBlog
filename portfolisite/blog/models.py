from django.db import models
from tinymce.models import HTMLField 

# Create your models here.
class Home(models.Model):
    hero_background_img = models.ImageField(upload_to="heroBackgroud", null=True, blank=True)
    hero_background_name = models.CharField(max_length=100, null=True, blank=True)
    site_name = models.CharField(max_length=100, null=True, blank=True)
    about_summary = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.hero_background_name


class Socials(models.Model):
    social_name = models.CharField(max_length=100, null=True, blank=True)
    social_icon = models.ImageField(upload_to="socials", null=True, blank=True)
    social_link = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.social_name

class Categories(models.Model):
    name = models.CharField(null=True, blank=True, max_length=300, unique=True)

    def __str__(self):
        return self.name

draft_publish = (
    ('publish','publish'),
    ('draft','draft'),
)

class Articles(models.Model):
    title = models.CharField(max_length=1000, null=True, blank=True)
    article_status = models.CharField(max_length=100, null=True, blank=True, choices=draft_publish)
    slug = models.CharField(max_length=1000, null=True, blank=True, unique=True)
    category = models.ManyToManyField(Categories, blank=True)
    lead_img = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    lead_img_thumbnail = models.ImageField(upload_to='media_files/blog', null=True, blank=True)
    lead_img_alt = models.CharField(max_length=1000, null=True, blank=True, help_text="alt text of an image")
    date_created = models.DateField(auto_now_add=True, null=True, blank=True)
    date_updated = models.DateField(null=True, blank=True)
    content = HTMLField()
    summary = models.TextField(null=True, blank=True, help_text="31 letters max will give a better out look")
    author = models.CharField(max_length=200, default="wise m", null=True, blank=True)
    author_image = models.ImageField(upload_to='media_files/authorImg', null=True, blank=True)
    author_image_thumbnail = models.ImageField(upload_to='media_files/authorImg', null=True, blank=True)
    author_image_atlt_text = models.CharField(max_length=1000, null=True, blank=True, help_text="alt text of an image")
    youtube_video_link = models.TextField(null=True, blank=True)
    num_views = models.CharField(max_length=30, null=True, blank=True)
    read_time = models.CharField(max_length=30, null=True, blank=True)
    # styleshit = models.CharField(max_length=100, null=True, blank=True, choices=choices, default="shades-of-purple.min.css")
    
    def __str__(self):
        return self.title
