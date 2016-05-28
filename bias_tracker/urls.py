"""bias_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(
        r'^accounts/login/$',
        auth_views.login,
        {'template_name': 'admin/login.html'}
    ),
    url(r'^$', views.render_index_page, name='index_page'),
    url(
        r'^new_incident$',
        views.render_new_incident_log_page,
        name='new_incident'
    ),
    url(r'^logout/', views.logout_return_home, name='logout'),
    url(r'^submit_new/', views.submit_new, name='submit_new'),
    url(r'^self_stats/', views.self_stats, name='self_stats')
    # url(r'', views.render_edit_incident_log_page, name='edit_incident'),
    # url(r'', views.render_statistics_view_page, name='statistics_page')
]
