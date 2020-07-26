from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from Blog.api import views
from Blog.api.views import PostDetail, PostList

urlpatterns = [
    path('', include('rest_framework.urls', namespace='rest_framework')),
    path('posts/', PostList.as_view()),
    path('posts/<int:pk>/', PostDetail.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)


# url for restframework API
# http://127.0.0.1:8000/Blog/api/posts/