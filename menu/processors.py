from menu.models import MenuItem

def get_menu(request):
	sidebar_items = MenuItem.objects.filter(menu = '0')
	main_items = MenuItem.objects.filter(menu = '1')
	return { 'sidebar_items':sidebar_items, 'main_items':main_items }