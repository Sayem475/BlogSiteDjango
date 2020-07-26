from django.shortcuts import render, redirect
from Blog.models import Post, BlogComment
from django.contrib import messages
from Blog.templatetags import extras
from django.core.paginator import Paginator

# Create your views here.
from django.views import View

class BlogHome(View):
    def get(self, request):
        post = Post.objects.all()

        paginator = Paginator(post, 6)
        page= request.GET.get('page')
        post= paginator.get_page(page)

        params = {'post': post}
        return render(request, 'Blog/bloghome.html', params)

class BlogPost(View):
    def get(self, request, slug):
        post = Post.objects.filter(slug=slug).first()
        comments = BlogComment.objects.filter(post=post, parent=None)
        replies = BlogComment.objects.filter(post=post).exclude(parent=None)
        repDict = {}
        for reply in replies:
            if reply.parent.sno not in repDict.keys():
                repDict[reply.parent.sno] = [reply]
            else:
                repDict[reply.parent.sno].append(reply)
        context = {'post': post, 'comments': comments,
                'user': request.user, 'repDict': repDict}
        return render(request, 'Blog/blogpost.html', context)

class PostComment(View):
    def post(self, request):
        # if request.method == 'POST':
            comment = request.POST.get('comment')

            user = request.user
            postsno = request.POST.get('postsno')
            post = Post.objects.get(sno=postsno)
            parentSno = request.POST.get('parentSno')
            if parentSno == "":
                comment = BlogComment(comment=comment, user=user, post=post)
                comment.save()
                messages.success(
                    request, 'Your comment has been successfully posted.')
            else:
                parent = BlogComment.objects.get(sno=parentSno)
                comment = BlogComment(
                    comment=comment, user=user, post=post, parent=parent)
                comment.save()
                messages.success(
                    request, 'Your reply has been successfully posted.')
            return redirect(f'/Blog/{post.slug}')
