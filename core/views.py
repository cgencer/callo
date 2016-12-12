from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from django.template import RequestContext
from rest_framework import generics
import requests
import json
import os
import sqlite3

from core import data
from core import menu
from core.models import UserProfile
from core.serializers import UserSerializer
from nutrition.models import CalorieInput, CalorieOutput

from core.forms import activitiesMade
from core.serializers import EmbedSerializer

def dashboard(request):
	cards = data.get_cards()
	menu_items = menu.get_menu_items('Dashboard')

	return render(request, 'dashboard.html', {
		'menu_items': menu_items,
		'cards': cards
	})


def activities(request):

	context = RequestContext(request)

	menu_items = menu.get_menu_items('Dashboard')
	with open(os.path.abspath('activities.json'), 'r') as data_file:
		activities = json.load(data_file)

	if request.method == "POST":

		form = activitiesMade(request.POST)

		if form.is_valid():
			form.save()

			return render(request, '5-activities.html', {
				'form': form,
				'menu_items': menu_items,
				'activities': activities
			})
		else:
			print(form.errors)
	else:
		form = activitiesMade()

	return render(request, '5-activities.html', {
		'form': form,
		'menu_items': menu_items,
		'activities': activities
	}, context)



def calories(request):

	context = RequestContext(request)

	menu_items = menu.get_menu_items('Dashboard')

	if request.method == "POST":

		form = activitiesMade(request.POST)

		if form.is_valid():
			form.save()

			return render(request, '7-consumption.html', {
				'form': form,
				'menu_items': menu_items,
			})
		else:
			print(form.errors)
	else:
		form = activitiesMade()

	return render(request, '7-consumption.html', {
		'form': form,
		'menu_items': menu_items,
	}, context)



def inout(request):

	menu_items = menu.get_menu_items('Dashboard')

	return render(request, '4-in-out.html', {
		'menu_items': menu_items
	})


def login(request):

	menu_items = menu.get_menu_items('Dashboard')

	return render(request, '2-login.html', {
		'menu_items': menu_items
	})


def mood(request):

	menu_items = menu.get_menu_items('Dashboard')

	return render(request, '8-mood.html', {
		'menu_items': menu_items
	})


def profile(request):

	context = RequestContext(request)

	menu_items = menu.get_menu_items('Profile')

	profile = {
		'name': 'Nur',
		'surname': 'Ertem Unden',
		'email': 'ertemnur@gmail.com',
		'description': 'some description',
		'age': '32',
		'birth': '24/04/1976',
		'bmi': 0,
		'weight': 70,
		'height': 175,
	}

	if request.method == "POST":

		form = saveProfile(request.POST)

		if form.is_valid():
			form.save()

			return render(request, '3-userinfo.html', {
				'form': form,
				'menu_items': menu_items,
				'profile': profile,
			})
		else:
			print(form.errors)
	else:
		form = saveProfile()

	return render(request, '3-userinfo.html', {
		'form': form,
		'profile': profile,
		'menu_items': menu_items
	}, context)


def settings(request):
	return render(request, 'temp/__settings.html')


class UserProfileView(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserSerializer
