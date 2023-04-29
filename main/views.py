from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from .forms import RegisterUserForm, LoginUserForm, AddPostForm
from .models import Posts

# Create your views here.


class MainHome(ListView):
    model = Posts
    template_name = 'main/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cut'] = 'home'
        context['cur_cat'] = 0
        return context

    def get_queryset(self):
        return Posts.objects.filter(is_published=True)


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'main/login.html'

    def get_success_url(self):
        return reverse_lazy('home')


class ShowPost(DetailView):
    model = Posts
    template_name = 'main/post.html'
    slug_url_kwarg = 'post_url'
    context_object_name = 'post'


class MainCategory(ListView):
    model = Posts
    template_name = 'main/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cur'] = 'home'
        context['cur_cat'] = self.kwargs['cat_url']
        return context

    def get_queryset(self):
        return Posts.objects.filter(cat__slug=self.kwargs['cat_url'], is_published=True)


class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


def logout_user(request):
    logout(request)
    return redirect('login')


class AddPost(LoginRequiredMixin, CreateView):
    form_class = AddPostForm
    template_name = 'main/add_post.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cut'] = 'home'
        return context
