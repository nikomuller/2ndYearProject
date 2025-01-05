from django.urls import path
from .views import (
    ArticleListView, 
    ArticleUpdateView, 
    ArticleDeleteView,
    ArticleDetailView,
    ArticleCreateView,
    CommentCreateView
)   

urlpatterns = [
    # 'commentnew/' to make it different from 'new/' of article_new so they wont get mixed up
    # order here matters as if new or comment new gets moved below slug, it'll become 'invisible' to django
    path('commentnew/', CommentCreateView.as_view(), name = "comment_new"),
    path('new/', ArticleCreateView.as_view(), name = 'article_new'),
    path('<slug:slug>/edit/', ArticleUpdateView.as_view(), name = 'article_edit'),
    path('<slug:slug>/', ArticleDetailView.as_view(), name = 'article_detail'),
    path('<slug:slug>/delete/', ArticleDeleteView.as_view(), name = 'article_delete'),
    path('', ArticleListView.as_view(), name = 'article_display'),
]