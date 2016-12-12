from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from nutrition.models import CalorieInput, CalorieOutput
from nutrition.serializers import CalorieInputSerializer, CalorieOutputSerializer
from nutrition.usda import UsdaFoodService


class CalorieInputListView(ListCreateAPIView):
	queryset = CalorieInput.objects.all().order_by('date')
	serializer_class = CalorieInputSerializer


class CalorieOutputListView(ListCreateAPIView):
	queryset = CalorieOutput.objects.all().order_by('date')
	serializer_class = CalorieOutputSerializer


class SearchFoodsView(APIView):

	def get(self, request):
		name = request.query_params.get('name')

		foods = []

		intakes = self.search_intakes(name)
		for intake in intakes:
			food = {
				"type": "I",
				"code": intake.code,
				"name": intake.name
			}
			foods.append(food)

		usdas = self.search_usda(name)
		for usda in usdas:
			food = {
				"type": "U",
				"code": usda["ndbno"],
				"name": usda["name"]
			}
			foods.append(food)

		return Response(foods)

	def search_intakes(self, name):
		intakes = CalorieInput.objects.filter(name__contains=name)
		return list(intakes)

	def search_recipes(self, name):
		recipes = []
		return list(recipes)

	def search_usda(self, name):
		try:
			foods = UsdaFoodService.search(name=name)
		except KeyError:
			foods = []
		return foods


class GetFoodNutrientsView(APIView):
	def get(self, request, code):
		try:
			ns = UsdaFoodService.get_nutrients(ndbno=code)
			nutrients = self.filter(ns)
		except KeyError:
			nutrients = []

		return Response(nutrients)

	def filter(self, ns, filter=False):
		if not filter:
			return ns

		VALID_NUTRIENTS = ['Energy', 'Protein', 'Calsium']

		nutrients = []
		for n in ns:
			if n['name'] in VALID_NUTRIENTS:
				nutrients.append(n)

		return nutrients


class GetFoodNutrientUnitsView(APIView):
	def get(self, request, code):
		units = UsdaFoodService.get_nutrient_units(ndbno=code)
		return Response(units)
