"""dashowl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('milestone/', include('dashowl.milestone.urls')),
    path('', include('dashowl.index.urls')),
    path('homepage/', include('dashowl.homepage.urls')),
    path('pullrequests/', include('dashowl.pull_requests.urls')),
    path('commits/', include('dashowl.commits.urls')),
    path('issues/', include('dashowl.issues.urls')),
    path('sprints/', include('dashowl.sprints.urls')),
    path('repositories/', include('dashowl.repositories.urls')),
    path('aboutus/', include('dashowl.politics.urls')),
    path('suport/', include('dashowl.suport.urls'))


]

