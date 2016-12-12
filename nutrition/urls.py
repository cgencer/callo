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
from nutrition import views

urlpatterns = [
	url(r"^food/$", views.SearchFoodsView.as_view()),
	url(r"^food/(?P<code>.+)/$", views.GetFoodNutrientsView.as_view()),
	url(r"^food/(?P<code>.+)/units/$", views.GetFoodNutrientUnitsView.as_view()),

	url(r"^in/$", views.CalorieInputListView.as_view()),
	url(r"^out/$", views.CalorieOutputListView.as_view()),
]
