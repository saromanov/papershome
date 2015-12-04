from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.views import generic
from django.views.generic import UpdateView, CreateView, ListView

from .models import Paper
from taggit.models import Tag

class AddPaperView(CreateView):
    model = Paper
    template_name = 'add_paper.html'

    def get_success_url(self):
        return reverse('paper-list')

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


def paper_page(request, paper_id):
    return HttpResponse("Page for the paper the id {0}".format(paper_id))
