"""dedupper_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from . import views

admin.autodiscover()

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^keys', views.upload, name='keys'),
    path('key/', views.key_gen, name='key'),
    # path('heroku/', generic.ListView.as_view(model=models.Contact), name='heroku'),
    path('run/', views.run, name='run'),
    path('map/', views.map, name='map'),
    path('login/', views.login, name='login'),
    path('upload_page/', views.upload_page, name='upload_page'),
    path('progress/', views.dup_progress, name='progress'),
    path('db_progress/', views.db_progress, name='db_progress'),
    path('closest/', views.closest, name='closest'),
    path('tables/', views.turn_table, name='tables'),
    path('import_csv/', views.import_csv, name='import_csv'),
    path('flush_db/', views.flush_db, name='flush_db'),
    path('resort/', views.resort, name='resort'),
    path('contact_sort/', views.contact_sort, name='contact_sort'), #figure out url reverse
    path('sorted/', views.display, name='reps'),
    path('sorted/<id>', views.merge, name='merge'),
    path('sorted/export/<type>', views.download, name='export'),
    path('sorted/report/<type>', views.download_times, name='report'),
]

