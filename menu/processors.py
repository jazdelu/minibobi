from menu.models import MenuItem

def get_menu(request):
	sidebar_items = MenuItem.objects.filter(menu__name = 'sidebar')
	main_items = MenuItem.objects.filter(menu__name = 'main')
	return { 'sidebar_items':sidebar_items, 'main_items':main_items }