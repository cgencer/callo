import requests


class UsdaFoodService(object):

	__api_base_url = 'http://api.nal.usda.gov/ndb/'
	__api_key = 't7dq28LzAEKWJUl3CcB2VIXPDvPBOlIVJYv0mKlW'
	__api_format = 'json'

	@staticmethod
	def __get_api_url(command):
		api_url = UsdaFoodService.__api_base_url + command + '/'
		api_url = api_url + '?api_key=' + UsdaFoodService.__api_key + \
							'&format=' + UsdaFoodService.__api_format
		return api_url

	@staticmethod
	def __get_report(ndbno):
		url = UsdaFoodService.__get_api_url('reports') + '&ndbno=' + ndbno + '&type=b'
		response = requests.get(url, allow_redirects=False)

		report = response.json()['report']['food']
		return report

	@staticmethod
	def __get_search(name):
		url = UsdaFoodService.__get_api_url('search') + '&q=' + name
		response = requests.get(url, allow_redirects=False)

		items = response.json()['list']
		return items

	@staticmethod
	def search(name):
		response = UsdaFoodService.__get_search(name)
		foods = response['item']
		return foods

	@staticmethod
	def get_nutrients(ndbno):
		response = UsdaFoodService.__get_report(ndbno)
		nutrients = response['nutrients']
		return nutrients

	@staticmethod
	def get_nutrient_units(ndbno):
		nutrients = UsdaFoodService.get_nutrients(ndbno)

		units = []
		for nutrient in nutrients:
			print(nutrient)
			for measure in nutrient['measures']:
				units.append(measure['label'])

		return set(units)

if __name__ == "__main__":
	foods = UsdaFoodService.search('apple')
	for food in foods:
		print(food)

	nutrients = UsdaFoodService.get_nutrients('43529')
	for nutrient in nutrients:
		print(nutrient)

	measures = UsdaFoodService.get_nutrient_units('43529')
	for measure in measures:
		print(measure)