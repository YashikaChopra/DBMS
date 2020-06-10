"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
from studs.api import ClassList, ParticularLocation

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^api/class_list/$', ClassList.as_view(), name='class_list'),
    url(r'^api/class_list/(?P<class_id>\d+)/$', ParticularLocation.as_view(), name='particular_location'),
    #url(r'^api/class_list/<str:NameOfClass>/$', ParticularLocation.as_view()),
]
