from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [

    # default page
    url(r'^$', views.index, name='index'),

    # Details page
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),

    # Favourite page for a music
    url(r'^(?P<album_id>[0-9]+)/favourite/$', views.favourite, name='favourite')
]
