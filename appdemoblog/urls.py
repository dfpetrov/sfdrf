from appdemoblog.views import PostList, PostDetail
from django.urls import path

app_name = 'appdemoblog'
urlpatterns = [
    path('', PostList.as_view(), name='post-list'),
    path('<int:pk>', PostDetail.as_view(), name='post-detail'),
]
