from django.shortcuts import render, redirect
from app_menus.forms import CategoryCreateForm, MenuCreateForm
from app_menus.models import Menu, Category

# Create your views here.
def list_menu(request):
    return render(request, 'menus/list_menu.html')

def add_menu(request):
    menu_create_form = MenuCreateForm() # creating Form Class object
    context = { "menu_create_form": menu_create_form, "title": "Create Menu here..." }

    if request.method == "POST":
        menu_title = request.POST.get('menu_title')
        menu_price = request.POST.get('menu_price')
        menu_ingredient = request.POST.get('menu_ingredient')
        category_obj = Category.objects.get(id=request.POST.get('menu_category'))
        #method one
        # menu_obj = Menu()
        # menu_obj.menu_title = menu_title
        # menu_obj.menu_price = menu_price
        # menu_obj.menu_category = category_obj # passing Category Object (Foreign Key Object)
        # menu_ingredient = menu_ingredient
        # menu_obj.save()
        # # method two
        # menu = Menu(menu_title=menu_title, menu_price=menu_price,
        #             menu_category=category_obj, menu_ingredient=menu_ingredient)
        # menu.save()

        # method three - storing data with Form Class Object
        menu = MenuCreateForm(request.POST)
        if menu.is_valid():
            menu.menu_category = category_obj
            menu.save()
            return redirect("menu-list")
        return redirect("menu-add")
    return render(request, 'menus/add_menu.html', context)