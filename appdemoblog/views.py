from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, FormView, ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django import views

from rest_framework import generics

from .models import Post, Author, Category
from .serializers import PostSerializer, CategorySerializer, CategorySerializer2
from .forms import CreatePostForm, CreateAuthorForm, CreateCategoryForm
from django.contrib.auth.models import User

class PostList(generics.ListAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return reverse_lazy('appdemoblog:post-list-alt')
    else:
        user_form = UserRegistrationForm()
    return render(request, 'appdemoblog/su.html', {'user_form': user_form})                                 

class PostEdit(CreateView):
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy('appdemoblog:post-list-alt')
    template_name = 'appdemoblog/create_post.html'

class PostListAlt(ListView):
    model = Post
    template_name = 'appdemoblog/post_list.html'
    context_object_name = 'posts'
    paginate_by = 3

class PostDetailAlt(DetailView):
    model = Post
    template_name = 'appdemoblog/post_detail.html'
    context_object_name = 'post'

class AuthorEdit(CreateView):
    model = Author
    form_class = CreateAuthorForm
    success_url = reverse_lazy('appdemoblog:author-list-alt')
    template_name = 'appdemoblog/create_author.html'

class AuthorListAlt(ListView):
    model = Author
    template_name = 'appdemoblog/author_list.html'
    context_object_name = 'authors'
    paginate_by = 3

class AuthorDetailAlt(DetailView):
    model = Author
    template_name = 'appdemoblog/author_detail.html'
    context_object_name = 'author'

class CategoryEdit(CreateView):
    model = Category
    form_class = CreateCategoryForm
    success_url = reverse_lazy('appdemoblog:category-list-alt')
    template_name = 'appdemoblog/create_category.html'

class CategoryListAlt(ListView):
    model = Category
    template_name = 'appdemoblog/category_list.html'
    context_object_name = 'categories'
    paginate_by = 20

class CategoryDetailAlt(DetailView):
    model = Category
    template_name = 'appdemoblog/category_detail.html'
    context_object_name = 'category'

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)

    if request.method == "POST":
        print('Создание категории:')
        # for i in range(101, 1000):            
        #     Category.objects.create(title=f"Фек-{i}", description='Lorem ipsum, dolor sit amet consectetur adipisicing elit')
        Category.objects.all()

    return render(request, 'appdemoblog/category_detail.html', {'category': category})

class CategoryListApi(generics.ListAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer2

class CategoryDetailApi(generics.RetrieveAPIView):  
    queryset = Category.objects.all()  
    serializer_class = CategorySerializer