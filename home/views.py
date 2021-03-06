from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views import generic
from django.views.generic import UpdateView, CreateView, ListView, View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login

from .models import Paper
from .forms import PaperForm, CodeForm
from taggit.models import Tag

class AddPaperView(CreateView):
    model = Paper
    template_name = 'add.html'
    fields = ['title', 'author', 'description', 'breif_description', 'version', 'category', 'link', 'repo','links']

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form': PaperForm(), 'code_form': CodeForm()})

    def post(self, request, *args, **kwargs):
        newpaper = Paper(request.POST)
        print("REQUEST: ", request.POST)
        #newpaper.save(commit=False)

class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = 'registration/login.html'
    success_url = '/'

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginView, self).form_valid(form)

class RegistrationView(FormView):
    form_class = UserCreationForm
    template_name = 'registration/registration_form.html'
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super(RegistrationView, self).form_valid(form)

class TagMixin(object):
    def get_content_data(self, kwargs):
        context = super(TagMixin, self).get_context_data(kwargs)
        context['tags'] = Tag.objects.all()
        return context

class IndexView(TagMixin, ListView):
    model = Paper
    content_object_name = 'paper_list'
    template_name = 'index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Paper.objects.order_by('-pubdate')[:5]


class PaperView(View):
    model = Paper
    template_name = 'paper.html'

    def get(self, request, paper_id, *args, **kwargs):
        paper = Paper.objects.get(uuid=paper_id)
        return render(request, self.template_name, {'paper': paper})

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name, {'paper': self.model})

#def paper_page(request, paper_id):
#    return HttpResponse("Page for the paper the id {0}".format(paper_id))
