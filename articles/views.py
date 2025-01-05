from django.db import models
from django.db.models import fields
from django.urls.base import reverse
from .models import Article, Comment
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = 'article_display.html'

class ArticleDetailView(DetailView, LoginRequiredMixin):
    model = Article
    template_name = 'article_detail.html'

class ArticleDeleteView(DeleteView, LoginRequiredMixin):
    model = Article
    template_name = 'article_detail.html'
    success_url = reverse_lazy('article_display')

class ArticleUpdateView(UpdateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    template_name = 'article_edit.html'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object
        return obj.author == self.request.user

class ArticleCreateView(CreateView, LoginRequiredMixin, UserPassesTestMixin):
    model = Article
    fields = ('title', 'body',)
    template_name = 'article_new.html'

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object
        return obj.author == self.request.user

class CommentCreateView(CreateView):
    model = Comment
    fields = ('article', 'body', 'rating')
    template_name = 'comment_new.html'
    success_url = reverse_lazy('article_display') 

    def form_valid(self, form):
        form.instance.author = self.request.user 
        return super().form_valid(form)

    def test_func(self):
        obj = self.get_object
        return obj.author == self.request.user