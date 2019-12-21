from django.shortcuts import render

from appdemoblog.models import Post  
from appdemoblog.serializers import PostSerializer  
from rest_framework import generics  


class PostList(generics.ListAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer

class PostDetail(generics.RetrieveAPIView):  
    queryset = Post.objects.all()  
    serializer_class = PostSerializer
