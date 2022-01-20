from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView

from blog.forms import CommentForm
from blog.models import Post


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.select_related('category').filter(category__slug=self.kwargs.get("slug"))


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"  # наименование объекта в шаблоне
    slug_url_kwarg = 'post_slug'  # переопределяем, т.к. дефотно айди

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


def index(request):
    return render(request, 'base.html')
