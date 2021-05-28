from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from blogging.models import Post
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


class BlogListView(ListView):
    model = Post
    template_name = 'blogging/list.html'

    def get_queryset(self):
        queryset = Post.objects.all()
        post = queryset.exclude(published_date__exact=None)
        published = post.order_by('-published_date')

        return published


class BlogDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if not self.object.published_date:
            raise Http404

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
