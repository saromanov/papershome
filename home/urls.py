from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^papers/(?P<paper_id>[0-9a-z-]+)/$', views.PaperView.as_view(), name='paper_page'),
]
