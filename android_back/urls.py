"""android_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from back import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^test/', views.hello_world, name='test'),
    url(r'^test1/', views.get_from_db, name='test1'),
    url(r'^fill/', views.fill_db, name='fill'),
    url(r'^words_list/', views.words_list, name='words list'),
    url(r'^decks_list/', views.decks_list, name='decks list'),
    url(r'^decks_content/', views.deck_content, name='decks content')
]
