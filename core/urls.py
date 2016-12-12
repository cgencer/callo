"""KarmaCircle URL Configuration

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
from core import views

app_name = "core"
urlpatterns = [
	url(r"^dashboard/$", views.dashboard, name='dashboard'),
	url(r"^activities/$", views.activities, name='activities'),
	url(r"^inout/$", views.inout, name='inout'),
	url(r"^calories/$", views.calories, name='inout'),
	url(r"^mood/$", views.mood, name='mood'),
	url(r"^login/$", views.login, name='login'),
	url(r"^profile/$", views.profile, name='profile'),

	url(r"^profile/$", views.UserProfileView.as_view()),
]
