from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add', views.AddPaperView.as_view(), name='add'),
    url(r'^accounts/login', views.LoginView.as_view(), name='login'),
    url(r'^accounts/register', views.RegistrationView.as_view(), name='registration'),
    url(r'^papers/(?P<paper_id>[0-9a-z-]+)/$', views.PaperView.as_view(), name='paper_page'),
]
