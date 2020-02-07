from django.conf.urls import url
from .views import(HomeView, ResultRedirectView)
from django.urls import path
urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^(?P<province>[\w-]+)/$', ResultRedirectView.as_view(), name='results'),
]