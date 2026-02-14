import os
from django.shortcuts import render
from rozwiazanie_weekend2 import DATA_DIR
from rozwiazanie_weekend2.pizza import Menu

MENU_FILE = os.path.join(DATA_DIR, 'menu.json')

def pizza_list(request):
    menu = Menu()
    menu.load_from_file(MENU_FILE)
    return render(request, 'menu_app/pizza_list.html', {'pizzas': list(menu)})