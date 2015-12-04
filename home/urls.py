from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<paper_id>[a-z]+)/$', views.paper_page, name='detail'),
]
