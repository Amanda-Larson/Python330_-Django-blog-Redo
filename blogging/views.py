from django.shortcuts import render
from blogging.models import Post
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView


# def list_view(request):
#     context = {'posts': Post.objects.all()}
#     return render(request, 'polling/list.html', context)


# def stub_view(request, *args, **kwargs):
#     body = "Stub View\n\n"
#     if args:
#         body += "Args:\n"
#         body += "\n".join(["\t%s" % a for a in args])
#     if kwargs:
#         body += "Kwargs:\n"
#         body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
#     return HttpResponse(body, content_type="text/plain")


# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.ordered_by('-published_date')
#     template = loader.get_template('blogging/list.html')
#     context = {'posts': posts}
#     body = template.render(context)
#     return HttpResponse(body, content_type="text/html")

class PostListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None).order_by('-published_date')
    template_name = 'blogging/list.html'


# this is a function that was changed into a class-based
# def list_view(request):
#     published = Post.objects.exclude(published_date__exact=None)
#     posts = published.order_by('-published_date')
#     context = {'posts': posts}
#     return render(request, 'blogging/list.html', context)

class PostDetailView(DetailView):
    model = Post
    template_name = 'blogging/detail.html'
    queryset = Post.objects.filter(published_date__isnull=False)



# def detail_view(request, post_id):
#     published = Post.objects.exclude(published_date__exact=None)
#     try:
#         post = published.get(pk=post_id)
#     except Post.DoesNotExist:
#         raise Http404
#     context = {'post': post}
#     return render(request, 'blogging/detail.html', context)
