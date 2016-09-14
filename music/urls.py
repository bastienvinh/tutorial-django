from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [

    # default page
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)$', views.DetailView.as_view(), name='detail')
]
