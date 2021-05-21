from django.db import models


# Create your models here.
class Cities(models.Model):
    city = models.CharField(max_length=200)

    def __str__(self):
        return self.city

class Categories(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class UserModel(models.Model):
    follower_count = models.IntegerField()
    following_count = models.IntegerField()
    name = models.CharField(max_length=200)
    category = models.ManyToManyField(Categories)
    bio = models.CharField(max_length=2000, blank=True)
    city = models.ManyToManyField(Cities)
    contact = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.name


