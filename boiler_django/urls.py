"""boiler_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
    path('app1/', include('app1.urls')),
    path('app2/', include('app2.urls')),
    path('app3/', include('app3.urls')),
    path('app4/', include('app4.urls')),
    path('app6/', include('app6.urls')),
    path('app8singleroute/', include('app8singleroute.urls')),
    path('app10srznomodel/', include('app10srznomodel.urls')),
    path('app12extrakw/', include('app12extrakw.urls')),
    path('app13multiple/', include('app13multiple.urls')),
    path('app13multiple/', include('app13multiple.urls')),
    path('app14kwargssrz/', include('app14kwargssrz.urls')),
    path('app15listfieldsample/', include('app15listfieldsample.urls')),
    path('app16templatingemail/', include('app16templatingemail.urls')),
    path('app9sampleroute/', include('app9sampleroute.urls')),
    path('app17apiviewsample/', include('app17apiviewsample.urls')),
    path('app20modelalt/', include('app20modelalt.urls')),
    path('app00starter/', include('app00starter.urls')),
    path('app21apiview/', include('app21apiview.urls')),
    path('paginate/', include('samplepaginate.urls')),
]
