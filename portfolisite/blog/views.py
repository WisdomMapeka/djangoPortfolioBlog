from django.shortcuts import render
from . models import Home, Categories, Articles, Socials

# Create your views here.

def index(request):
    home = Home.objects.all().order_by("-id").first()
    recent_articles = Articles.objects.all().order_by("-id")[:3]
    socials = Socials.objects.all().order_by("-id")[:4]
    return render(request, "blog/home.html", {"recent_articles":recent_articles,
                                            "socials":socials,
                                            "home":home})