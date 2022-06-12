#!/usr/bin/python3
from importlib.resources import path
from random import random
from django.urls import Li

from django.shortcuts import render
from django.http import HttpResponse

from .models import User, Interests
from gnews import GNews
from linkpreview import link_preview

#def aggregate(interests):
def aggregate():
    """    
    still have no users yet so let's make it general
    basically 20'%' sports 30'%' politics 50'%' tech
    interests = Interests.objects.filter(usr.email)
    """
    r = []
    google_news = GNews(language='en', Country='US', period='5d',  max_result=100)
    news_urls = google_news.get_news('Sports',  max_result=20)
    r.extend(news_urls)
    news_urls = google_news.get_news('Tunisia', max_result=30)
    r.extend(news_urls)
    news_urls = google_news.get_news('Software Engineering', max_result=50)
    r.extend(news_urls)
    random.shuffle(r)
    return r



# Create your views here.
def fetch_previews(request):
    articles = aggregate()
    for url in articles:
    #check 

    #for i in interests:
        #news_urls = google_news.get_news(i, max_result=)
    #will complete this when i make users and a user class in tests 
    previews = [link_preview(preview) for preview in articles]
    context{'articles': articles}
    return render(requset, 'homepage.html', context=context)
    
""""
class HomePageView(ListView):
    template_name = "home_page"
    model = Interests
    """
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        previews = fetch_previews()
        context["previews"] =  previews
        return context
        """
    
    