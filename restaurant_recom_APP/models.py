from django.db import models

# Create your models here.

class Cities(models.Model):
    id = models.AutoField(primary_key=True)
    city_name = models.CharField(max_length=100)


class Restaurant_Details(models.Model):
    montant = models.CharField(max_length=100)
    cuisine = models.CharField(max_length=150)
    top_food=models.CharField(max_length=150)

class Restaurant(models.Model):
    id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    review = models.CharField(max_length=30)
    rating = models.FloatField()
    long = models.CharField(max_length=20)
    lat = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    status = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    restaurant_details = models.OneToOneField(Restaurant_Details,on_delete=models.CASCADE)
    city = models.ForeignKey(Cities,on_delete=models.CASCADE)


class Image(models.Model):
    img_link = models.CharField(max_length=250)
    restaurant = models.ForeignKey(Restaurant,on_delete=models.CASCADE)






