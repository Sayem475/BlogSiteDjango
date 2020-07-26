from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from home.models import *
from home.models import jsdescription
from Blog.models import Post
from django.core.paginator import Paginator

from django.views import View
from django.views.generic import TemplateView


# Create your views here.

class Home(View):
    def get(self, request):
        designs = design.objects.all()
        freqques = FAQ.objects.all()
        param = {'designs': designs, 'freques': freqques}
        return render(request, 'home/home.html', param)

class ContactView(View):
    def get(self, request):
        return render(request, 'home/contact.html')

    def post(self, request):
        # if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']

        if len(name) < 3 or len(email) < 5 or len(phone) < 8 or len(msg) < 10:
            messages.error(request, 'Please fill the form Correctly.')
        else:
            contacts = Contact(name=name, email=email, phone=phone, msg=msg)
            contacts.save()
            messages.success(request, 'Congratulations! Your message has been sent Successfully...')
        return render(request, 'home/contact.html')


class AboutView(TemplateView):
    template_name = 'home/about.html'
    # def about(request):
    #     return render(request, 'home/about.html')

class Search(View):
    def get(self, request):
        query = request.GET['query']
        if len(query) > 50:
            posts = []
            messages.error(request, 'Sorry! Keywords is too long, No Search Results Found.')
        elif len(query) == 0:
            posts = []
            messages.warning(request, 'Invalid! Make sure to enter at least 4 characters')
        else:
            postTitle = Post.objects.filter(title__icontains=query)
            postContent = Post.objects.filter(content__icontains=query)
            posts = postTitle.union(postContent)
        # if posts.count()==0:
        #     messages.error(request,'No Search Results Found. Please Fill The Form Correctly')
        params = {'posts': posts, 'query': query}
        return render(request, 'home/search.html', params)

class HandleSignup(View):
    def get(self, request):
        return HttpResponse('404- Not Found')

    def post(self, request):
        # if request.method == 'POST':
            username = request.POST['username']
            f_name = request.POST['f_name']
            l_name = request.POST['l_name']
            email = request.POST['email']
            pas1 = request.POST['pas1']
            pas2 = request.POST['pas2']

            if len(username) > 10:
                messages.error(request, ' Username must be under 10 characters.')
                return redirect('home')
            if not username.isalnum():
                messages.error(
                    request, ' Username must contain alphanumeric values.')
                return redirect('home')
            if pas1 != pas2:
                messages.error(request, " Passwords didn't match.")
                return redirect('home')

            myuser = User.objects.create_user(username, email, pas1)
            myuser.first_name = f_name
            myuser.last_name = l_name
            myuser.save()
            messages.success(
                request, 'Congratulations! your account has been created successfully.')
            return render(request, 'home/home.html')
            

class HandleLogin(View):
    def get(self, request):
        return HttpResponse('404- Not Found')
    def post(self, request):
        # if request.method == 'POST':
            usname = request.POST['usname']
            pas = request.POST['pas']

            user = authenticate(username=usname, password=pas)
            if user is not None:
                login(request, user)
                messages.success(request, " You are successfully logged in.")
                return render(request, 'home/home.html')

            else:
                messages.error(request, " Opps! Something wrong, Please try again.")
                return render(request, 'home/home.html')
            

class HandleLogout(View):
    def get(self, request):
        logout(request)
        messages.info(request, 'You are successfully logged out.')
        return redirect('home')

class LearnView(TemplateView):
    template_name = 'home/learn.html'
    # def learn(request):
    #     return render(request, 'home/learn.html')

class HTMLPage(View):
    def get(self,request):
        chapter = htmlchapters.objects.all()
        desc = None
        chapterSNO = request.GET.get('chaptersno')
        if chapterSNO:
            desc = htmldescription.objects.filter(sno__icontains=chapterSNO)
        else:
            desc = htmldescription.objects.all()
        context = {'chapters': chapter, 'desc': desc}
        return render(request, 'home/hypert.html', context)

class CascadPage(View):
    def cascadpage(self, request):
        chapter = csschapters.objects.all()
        desc = None
        chapterSNO = request.GET.get('chaptersno')
        if chapterSNO:
            desc = cssdescription.objects.filter(sno__icontains=chapterSNO)
        else:
            desc = cssdescription.objects.all()
        context = {'chapters': chapter, 'desc': desc}
        return render(request, 'home/cascad.html', context)

class JavaPage(View):
    def get(self, request):
        chapter = jschapters.objects.all()
        desc = None
        chapterSNO = request.GET.get('chaptersno')
        if chapterSNO:
            desc = jsdescription.objects.filter(sno__icontains=chapterSNO)
        else:
            desc = jsdescription.objects.all()
        context = {'chapters': chapter, 'desc': desc}
        return render(request, 'home/javasc.html', context)

class PyPage(View):
    def get(self, request):
        chapter = pychapters.objects.all()
        desc = None
        chapterSNO = request.GET.get('chaptersno')
        if chapterSNO:
            desc = pydescription.objects.filter(sno__icontains=chapterSNO)
        else:
            desc = pydescription.objects.all()
        context = {'chapters': chapter, 'desc': desc}
        return render(request, 'home/python.html', context)

class DjPage(View):
    def get(self,request):
        chapter = djchapters.objects.all()
        desc = None
        chapterSNO = request.GET.get('chaptersno')
        if chapterSNO:
            desc = djdescription.objects.filter(sno__icontains=chapterSNO)
        else:
            desc = djdescription.objects.all()
        context = {'chapters': chapter, 'desc': desc}
        return render(request, 'home/django.html', context)
