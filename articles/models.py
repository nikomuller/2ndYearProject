from django.conf import settings
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField(null=True, unique=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    
    class Meta:
        ordering = ['-date'] # filters posts by date

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article,self).save(*args,**kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('article_detail', args = [str(self.slug)])

class RestrictedRatings(models.PositiveIntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        # ^ defines the parameters, but sets them as none for now
        self.min_value, self.max_value = min_value, max_value
        # ^ allows the local variables to be used elsewhere
        models.PositiveIntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(RestrictedRatings, self).formfield(**defaults)

class Comment(models.Model):
    body = models.TextField(max_length=2000)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    article=models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments',
    
    )
    rating = RestrictedRatings(min_value = 1, max_value=5, default=1, null=True, blank=True)
    # large comment section to accomadate various types of comments

class Meta: #orders the comments by rating from highest to lowest
    ordering = ['-rating']

    def __str__(self):
        return self.body

    def get_absolute_url(self): 
        return reverse('article_display', args=[str(self.id)])
