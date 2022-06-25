from django.shortcuts Import render
from django.urls Import reverse lazy
from django.views.generic.list inport ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail Import Detallview
from models import Post
# Create your views here.


class PostListView(ListView):

    # specify the model for list view
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    fields = "___all___"
    success_url = reverse_lazy("blog:all")


class PostDeleteView(UpdateView):
    model = Post
    fields = "_all_"
    success_url = reverse_lazy("blog:all")
