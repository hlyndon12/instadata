import instaloader
import csv


def followers(name):
    city_list = []
    with open('static_project/worldcities.csv', encoding="utf8" ,newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            if row['country'] == 'India':
                city_list.append(row['city_ascii'])
    
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(
        L.context, name)
    category = ''
    if profile.is_business_account:
        category = profile.business_category_name

    follower = profile.followers
    followee = profile.followees
    user = profile.username
    bio = profile.biography
    return follower, followee, user, bio, category
