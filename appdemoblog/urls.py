from django.urls import path
from django.conf.urls import url
from .views import PostList, PostDetail, PostEdit, PostListAlt, PostDetailAlt, AuthorEdit, AuthorDetailAlt, AuthorListAlt, CategoryEdit, CategoryListAlt, CategoryDetailAlt, category_detail, register, CategoryListApi, CategoryDetailApi

app_name = 'appdemoblog'

urlpatterns = [
    path('postJSON', PostList.as_view(), name='post-json'),
    path('', PostListAlt.as_view(), name='post-list'),
    # path('<int:pk>', PostDetail.as_view(), name='post-detail'),
    
    path('post/create', PostEdit.as_view(), name='post-create'),
    path('posts', PostListAlt.as_view(), name='post-list-alt'),
    url(r'^posts/(?P<slug>[-\w]+)/$', PostDetailAlt.as_view(), name='post-detail-alt'),

    path('author/create', AuthorEdit.as_view(), name='author-create'),
    path('authors', AuthorListAlt.as_view(), name='author-list-alt'),
    url(r'^authors/(?P<slug>[-\w]+)/$', AuthorDetailAlt.as_view(), name='author-detail-alt'),

    path('category/create', CategoryEdit.as_view(), name='category-create'),
    # path('categories', CategoryListAlt.as_view(), name='category-list-alt'),
    path('categories2', CategoryListAlt.as_view(), name='category-list2'),
    # path('categories/<int:pk>/', category_detail, name='category-detail'),
    path('categories2/<int:pk>/', category_detail, name='category-detail'),
    # url(r'^categories/(?P<slug>[-\w]+)/$', CategoryDetailAlt.as_view(), name='category-detail-alt'),
    url(r'^categories2/(?P<slug>[-\w]+)/$', CategoryDetailAlt.as_view(), name='category-detail-alt'),

    

    # API
    path('categories', CategoryListApi.as_view(), name='category-list-api'),
    path('categories/<int:pk>/', CategoryDetailApi.as_view(), name='category-detail-api'),

    path('su', register, name='su'),
]
