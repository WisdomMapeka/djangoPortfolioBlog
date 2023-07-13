from django.contrib import admin
from .models import Categories, Articles, Home, Socials

# Register your models here.
admin.site.register(Home)
admin.site.register(Categories)
admin.site.register(Articles)
admin.site.register(Socials)
