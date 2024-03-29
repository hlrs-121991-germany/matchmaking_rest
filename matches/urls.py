from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from matches import views as matches_views


urlpatterns = [
    url(r'^position/(?P<slug>[\w-]+)/$', matches_views.position_match_view, name='position_match_view_url'),
    url(r'^employer/(?P<slug>[\w-]+)/$', matches_views.employer_match_view, name='employer_match_view_url'),
    url(r'^location/(?P<slug>[\w-]+)/$', matches_views.location_match_view, name='location_match_view_url'),
]

