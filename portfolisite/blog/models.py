from django.db import models

# Create your models here.
class Home(models.Model):
    hero_background_img = models.ImageField(upload_to="heroBackgroud", null=True, blank=True)
    hero_background_name = models.CharField(max_length=100, null=True, blank=True)
    site_name = models.CharField(max_length=100, null=True, blank=True)
    about_summary = models.CharField(max_length=400, null=True, blank=True)

    social1_name = models.CharField(max_length=100, null=True, blank=True)
    social1_icon = models.ImageField(upload_to="socials", null=True, blank=True)

    social2_name = models.CharField(max_length=100, null=True, blank=True)
    social2_icon = models.ImageField(upload_to="socials", null=True, blank=True)

    social3_name = models.CharField(max_length=100, null=True, blank=True)
    social3_icon = models.ImageField(upload_to="socials", null=True, blank=True)

    social4_name = models.CharField(max_length=100, null=True, blank=True)
    social4_icon = models.ImageField(upload_to="socials", null=True, blank=True)

    def __str__(self):
        return self.hero_background_name

