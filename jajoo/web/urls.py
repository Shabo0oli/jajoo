from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^accounts/register/?$', views.register, name='register'),
    url(r'^accounts/login/?$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^place/([0-9]*)/$', views.place, name='place'),
    url(r'^search/$', views.search, name='search'),
    url(r'^comment/$', views.comment, name='comment'),
    url(r'^booking/$', views.booking, name='booking'),
    url(r'^$', views.index, name='index'),
]
