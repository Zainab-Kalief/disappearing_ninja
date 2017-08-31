from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas$', views.ninja),
    url(r'^(?P<word>\w+)/$', views.ninjas),
]
