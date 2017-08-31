from django.conf.urls import url,include

urlpatterns = [
    url(r'^', include('apps.ninja2_app.urls')),
]
