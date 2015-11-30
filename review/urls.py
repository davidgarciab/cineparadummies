from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.review_list),
    url(r'^review/(?P<pk>[0-9]+)/$', views.review_detail),
]
