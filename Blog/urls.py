from django.urls import path, include
from . import views
from django.views import View
from .views import BlogHome, BlogPost,PostComment

urlpatterns = [
    path('postComment', PostComment.as_view(), name='postComment'),
    path('', BlogHome.as_view(), name='blogHome'),
    path('<str:slug>', BlogPost.as_view()),
    path('api/', include('Blog.api.urls')),
   
]
