from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import  Restaurant, Image


#Get list of restaurants

@csrf_exempt
def get_restaurants(request):

    restaurants = Restaurant.objects.all()

    data = []
    for restaurant in restaurants:
        images = Image.objects.filter(restaurant=restaurant)
        details = restaurant.restaurant_details
        city = restaurant.city
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'review': restaurant.review,
            'rating': restaurant.rating,
            'longitude': restaurant.long,
            'latitude': restaurant.lat,
            'address': restaurant.address,
            'status': restaurant.status,
            'phone': restaurant.phone,
            'cuisine': details.cuisine,
            'top_food': details.top_food,
            'city': city.city_name,
            'images': [image.img_link for image in images],
        }
        data.append(restaurant_data)


    return JsonResponse(data, safe=False)

#Get restaurants by id
@csrf_exempt
def get_restaurant_by_id(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)

    images = Image.objects.filter(restaurant=restaurant)
    details = restaurant.restaurant_details
    city = restaurant.city
    restaurant_data = {
        'id': restaurant.id,
        'name': restaurant.name,
        'review': restaurant.review,
        'rating': restaurant.rating,
        'longitude': restaurant.long,
        'latitude': restaurant.lat,
        'address': restaurant.address,
        'status': restaurant.status,
        'phone': restaurant.phone,
        'cuisine': details.cuisine,
        'top_food': details.top_food,
        'city': city.city_name,
        'images': [image.img_link for image in images],
    }

    return JsonResponse(restaurant_data)

#Get restaurants by name
@csrf_exempt
def get_restaurant_by_name(request, name):
    restaurants = Restaurant.objects.filter(name__icontains=name)

    data = []
    for restaurant in restaurants:
        images = Image.objects.filter(restaurant=restaurant)
        details = restaurant.restaurant_details
        city = restaurant.city
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'review': restaurant.review,
            'rating': restaurant.rating,
            'longitude': restaurant.long,
            'latitude': restaurant.lat,
            'address': restaurant.address,
            'status': restaurant.status,
            'phone': restaurant.phone,
            'cuisine': details.cuisine,
            'top_food': details.top_food,
            'city': city.city_name,
            'images': [image.img_link for image in images],
        }
        data.append(restaurant_data)

    return JsonResponse(data, safe=False)



#Get restaurants by City name
@csrf_exempt
def get_restaurants_by_city(request, city):
    restaurants = Restaurant.objects.filter(city__city_name__iexact=city)

    data = []
    for restaurant in restaurants:
        images = Image.objects.filter(restaurant=restaurant)
        details = restaurant.restaurant_details
        city = restaurant.city
        restaurant_data = {
            'id': restaurant.id,
            'name': restaurant.name,
            'review': restaurant.review,
            'rating': restaurant.rating,
            'longitude': restaurant.long,
            'latitude': restaurant.lat,
            'address': restaurant.address,
            'status': restaurant.status,
            'phone': restaurant.phone,
            'cuisine': details.cuisine,
            'top_food': details.top_food,
            'city': city.city_name,
            'images': [image.img_link for image in images],
        }
        data.append(restaurant_data)

    return JsonResponse(data, safe=False)