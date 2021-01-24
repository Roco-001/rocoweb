from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic.list import ListView
from .models import Post, Category

# Create your views here.
class PostListView(ListView):
    model = Post
    paginate_by = 3

def blog(request, post_id, post_slug):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'pages/blog.html', {'post':post})


def category(request, category_id, category_slug):
    category = get_object_or_404(Category, id=category_id)
    return render(request, "pages/category.html", {'category':category})