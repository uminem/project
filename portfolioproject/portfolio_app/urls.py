from django.urls import path
from portfolio_app import views
from django.conf.urls import url

app_name = 'portfolio_app'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('contact/', views.contact, name = 'contact'),
    path('blog/', views.blog, name = 'blog'),
    path('create/', views.article_create, name ='create'),
    path('<slug>/', views.article_detail, name = 'detail'),
    
]
