from appdemoblog.models import Post, Category, Author
from rest_framework import serializers
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        # fields = ['name', 'description', 'last_name']
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):

    author = AuthorSerializer(required=False)
    category = CategorySerializer(required=False, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'

class CategorySerializer2(serializers.ModelSerializer):
    
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = ['id', 'title', 'description', 'slug', 'posts']