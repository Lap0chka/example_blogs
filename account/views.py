from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from blog.models import Post
from blog.forms import PostForm, PostChangeForm
from django.views.generic.edit import CreateView, UpdateView



@login_required
def dashboard(request):
    posts = Post.published.filter(author=request.user)
    best_posts = Post.published.order_by('-view')[:3]
    return render(request, 'base.html', {'best_posts': best_posts, 'posts':posts})

@login_required
def add_post(request):
    form = PostForm
    posts = Post.objects.filter(author=request.user)
    return render(request, 'account/add_post.html', {'form': form, 'posts':posts})


def post_edit(request, year, month, day, post):
    form = PostChangeForm
    post = get_object_or_404(Post,status=Post.Status.PUBLISHED,
                             slug=post, publish__year=year, publish__month=month, publish__day=day)
    #view
    post.view += 1
    post.save()
    # Список активных комментариев к этому посту


    return render(request, 'account/edit.html', {
        'post': post,
        'form': form,
    })

class PostEditView(UpdateView):
    model = Post
    form_class = PostChangeForm
    template_name = 'account/edit.html'

    def get_object(self, queryset=None):
        # ваш код получения объекта по переданным параметрам year, month, day и post
        # например:
        year = self.kwargs['year']
        month = self.kwargs['month']
        day = self.kwargs['day']
        post_slug = self.kwargs['post']
        return Post.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=post_slug)










