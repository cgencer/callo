

def get_cards():
	cards = []

	card1 = {
		'title': 'Weight',
		'value': '81',
		'unit': 'kg',
		'comment': 'today',
		'icon1': 'ti-server',
		'icon2': 'ti-reload'
	}
	cards.append(card1)
	card2 = {
		'title': 'BMI',
		'value': '24.5',
		'unit': '',
		'comment': 'today',
		'icon1': 'ti-pulse',
		'icon2': 'ti-reload'
	}
	cards.append(card2)
	card3 = {
		'title': 'Intake',
		'value': '2250',
		'unit': 'cal',
		'comment': 'today',
		'icon1': 'ti-pulse',
		'icon2': 'ti-reload'
	}
	cards.append(card3)
	card4 = {
		'title': 'Outtake',
		'value': '750',
		'unit': 'cal',
		'comment': 'today',
		'icon1': 'ti-pulse',
		'icon2': 'ti-reload'
	}
	cards.append(card4)
	return cards
