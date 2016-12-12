from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
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

from core.forms import SubmitEmbed
from core.serializers import EmbedSerializer

def dashboard(request):
	cards = data.get_cards()
	menu_items = menu.get_menu_items('Dashboard')

	return render(request, 'dashboard.html', {
		'menu_items': menu_items,
		'cards': cards
	})


def activities(request):

	menu_items = menu.get_menu_items('Dashboard')
	with open(os.path.abspath('activities.json'), 'r') as data_file:
		activities = json.load(data_file)

	if request.method == "POST":
'''
		conn = sqlite3.connect(os.path.abspath('data/db.sqlite3'))
		c = conn.cursor()
'''
		form = SubmitEmbed(request.POST)
		if form.is_valid():
			url = form.cleaned_data['url']
'''
			r = requests.get('http://api.embed.ly/1/oembed?key=' + settings.EMBEDLY_KEY + '&url=' + url)
			jsonized = r.json()
			serializer = EmbedSerializer(data=jsonized)
			if serializer.is_valid():
				embed = serializer.save()
'''
				instance = form.save(commit=False)
				instance.saveform = activitiesMade.objects.get(title=offset)
				instance.save()

				return render(request, '5-activities.html', {
					'embed': embed,
					'menu_items': menu_items,
					'activities': activities
				})
	else:
		form = SubmitEmbed()

	return render(request, '5-activities.html', {
		'form': form,
		'menu_items': menu_items,
		'activities': activities
	})



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


def timeline(request):
	menu_items = menu.get_menu_items('Timeline')

	intakes = CalorieInput.objects.all()
	outtakes = CalorieOutput.objects.all()

	return render(request, 'timeline.html', {
		'menu_items': menu_items,
		'intakes': intakes,
		'outtakes': outtakes
	})


def profile(request):
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

	return render(request, '3-userinfo.html', {
		'profile': profile,
		'menu_items': menu_items
	})

def settings(request):
	return render(request, 'temp/__settings.html')


class UserProfileView(generics.ListCreateAPIView):
	queryset = UserProfile.objects.all()
	serializer_class = UserSerializer
