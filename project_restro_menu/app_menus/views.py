from django.shortcuts import render
from app_menus.forms import CategoryCreateForm, MenuCreateForm

# Create your views here.
def list_menu(request):
    return render(request, 'menus/list_menu.html')

def add_menu(request):
    menu_create_form = MenuCreateForm() # creating Form Class object
    context = { "menu_create_form": menu_create_form, "title": "Create Menu here..." }
    return render(request, 'menus/add_menu.html', context)