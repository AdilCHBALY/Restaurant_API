from django.urls import re_path
from restaurant_recom_APP import RestController

urlpatterns = [
    #patient urls
    re_path(r'^restaurant$',RestController.get_restaurants),
    re_path(r'^restaurant/([0-9]+)$',RestController.get_restaurant_by_id),
    #rdv urls
    re_path(r'^city$',RestController.get_city),
    re_path(r'^city/([0-9]+)$',RestController.get_city_by_id),
]