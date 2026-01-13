from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant
from .forms import RestaurantForm

# ===== Список ресторанов + поиск =====
def restaurant_list(request):
    query = request.GET.get('q')
    if query:
        restaurants = Restaurant.objects.filter(specialty__icontains=query)
    else:
        restaurants = Restaurant.objects.all()
    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants, 'query': query})

# ===== Детали ресторана =====
def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    return render(request, 'restaurants/restaurant_detail.html', {'restaurant': restaurant})

# ===== Создание ресторана =====
def restaurant_create(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/restaurant_form.html', {'form': form})

# ===== Редактирование ресторана =====
def restaurant_update(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_detail', restaurant_id=restaurant.id)
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurants/restaurant_form.html', {'form': form})

# ===== Удаление ресторана =====
def restaurant_delete(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, 'restaurants/restaurant_confirm_delete.html', {'restaurant': restaurant})
