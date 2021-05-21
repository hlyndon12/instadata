from django.shortcuts import render, redirect
from .content import followers
import csv
from .models import UserModel, Cities,Categories
import re
from django.core.paginator import Paginator
from .filters import FollowerFilter
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required
def home(request):


    

    count_filter = FollowerFilter(request.GET)
    p = Paginator(count_filter.qs, 10)
    page_number = request.GET.get('page')
    page_obj = p.get_page(page_number)
    return render(request, 'main/main.html', {
        'data': page_obj,
        'range': count_filter
    })


def update(request):
    
    with open('static_project/urls.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            name = row['ï»¿Instagram URL'].split('/')[3]
            a = followers(name)
            query_all = UserModel.objects.all()
            category = Categories.objects.all()
            if category.filter(category=a[4]).exists() == False:
                new_category = Categories(category=a[4])
                new_category.save()
            if query_all.filter(name=a[2]).exists():
                
                contact = ''
                ls = re.findall('\S+@\S+', a[3])
                for obj in ls:
                    contact = contact + obj
                q = UserModel.objects.get(name=a[2])
                q.contact = str(contact)
                q.follower_count = a[0]
                q.following_count = a[1]
                q.bio = a[3]
                category = Categories.objects.get(category=a[4])
                q.category.add(category)
                print(q.name+a[4])
                q.save()
            else:
                print(a[2])
                new = UserModel(follower_count=a[0],
                                following_count=a[1],
                                name=a[2],
                                bio=a[3],
                                )
                new.save()
    return redirect('/')

def update_city(request):
    city_list = []
    with open('static_project/worldcities.csv', encoding="utf8" ,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['country'] == 'India':
                city_list.append(row['city_ascii'])
    l = UserModel.objects.all()
    for objects in l:
        name = objects.name
        bio = objects.bio
        for city in city_list:
            c_list = Cities.objects.all()
            if bio.find(city) != -1:
                if c_list.filter(city=city).exists() == False:
                    new_city = Cities(city=city)
                    new_city.save()
                city = Cities.objects.get(city=city)
                user = UserModel.objects.get(name=name)
                user.city.add(city)

               
                

    

    return redirect('/')
