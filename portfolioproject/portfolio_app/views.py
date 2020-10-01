from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.core.mail import send_mail
from django.contrib import messages
from django.template.loader import get_template
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms
from portfolio_app.forms import ContactForm


# Create your views here.
def index (request):
    return render(request, 'portfolio_app/index.html')

def about (request):
    return render(request, 'portfolio_app/index.html')

def blog (request):
    articles = Article.objects.all().order_by('date')
    return render(request, 'portfolio_app/blog.html', {'articles':articles})

def article_detail (request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'portfolio_app/blog_detail.html', {'article':article})

@login_required(login_url='/accounts/login/')
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            int = form.save(commit=False)
            int.author = request.user
            int.save()
            return redirect('portfolio_app:blog')
    else: 
        form = forms.CreateArticle()
    return render(request, 'portfolio_app/article_create.html', {'form':form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data ['name']
            email = form.cleaned_data ['email']
            subject = form.cleaned_data ['subject']
            message = form.cleaned_data ['message']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['isikaume@gmail.com']
            if cc_myself:
                recipients.append(email)

            send_mail(name, email, subject, message, recipients, fail_silently=True)
            messages.success(request, "Your Message has been sent Successfully. Thank You!")
            form = ContactForm()
    else:
        form = ContactForm()
    return render(request, 'portfolio_app/index.html', {'form': form})
       