
def get_menu_items(active_menu='Dashboard'):
	menu_items = []

	menu1 = {
		'active': 'active' if active_menu == 'Dashboard' else '',
		'class': 'ti-panel',
		'name': 'Dashboard',
		'link': '/core/dashboard'
	}
	menu_items.append(menu1)

	menu2 = {
		'active': 'active' if active_menu == 'Timeline' else '',
		'class': 'ti-text',
		'name': 'Timeline',
		'link': '/core/timeline'
	}
	menu_items.append(menu2)

	menu3 = {
		'active': 'active' if active_menu == 'Profile' else '',
		'class': 'ti-user',
		'name': 'Profile',
		'link': '/core/profile'
	}
	menu_items.append(menu3)

	return menu_items
