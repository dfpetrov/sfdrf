from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

def get_unique_slug(model, title):
    slug = slugify(title, allow_unicode=True)
    unique_slug = slug
    num = 1
    while model.objects.filter(slug=unique_slug).exists():
        unique_slug = f"{slug}-{num}"
        num += 1
    return unique_slug

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название категории')
    description = models.TextField(null=True, default=None, blank=True, verbose_name='Описание категории')
    slug = models.SlugField(null=True, default=None, unique=True, blank=True)
    def get_absolute_url(self):
        return reverse('appdemoblog:category-detail-alt', args=[str(self.slug)])

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(Category, self.title)
        super().save(*args, **kwargs)

class Author(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    avatar = models.ImageField(upload_to='appdemoblog/images/authors/', verbose_name='Аватар')
    description = models.TextField(verbose_name='О себе')
    slug = models.SlugField(null=True, default=None, unique=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('appdemoblog:author-detail-alt', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(Author, self.name)
        super().save(*args, **kwargs)
        
class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название статьи')
    slug = models.SlugField(null=True, default=None, unique=True, blank=True)
    status = models.CharField(max_length=10, choices=[('D', 'draft'), ('P', 'published')], verbose_name='Статус')
    content = models.TextField(verbose_name='Текст статьи')
    updated = models.DateTimeField(default=timezone.now)
    publication_date = models.DateTimeField(default=timezone.now)
    # category = models.ManyToManyField(Category, verbose_name='Категория')
    category = models.ForeignKey(Category, null=True, default=None, on_delete=models.SET_NULL, verbose_name='Категория', related_name='posts')
    author = models.ForeignKey(Author, null=True, default=None, on_delete=models.SET_NULL, verbose_name='Автор')
    img = models.ImageField(upload_to='appdemoblog/images/posts/', verbose_name='Основное изображение')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('appdemoblog:post-detail-alt', args=[str(self.slug)])

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = get_unique_slug(Post, self.title)
        super().save(*args, **kwargs)