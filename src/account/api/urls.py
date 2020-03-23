from django.conf.urls import url,include
from tweets.api.views import TweetListAPIView
	
	
from django.views.generic.base import RedirectView

urlpatterns = [
	  # url(r'^', include('django.contrib.auth.urls')),
      url(r'^(?P<username>[\w.@+-]+)/tweet/$', TweetListAPIView.as_view(),name='list'),#/api/tweet/
      
    ]


