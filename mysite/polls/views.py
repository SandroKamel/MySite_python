from django.shortcuts import render
from django.http import HttpResponse
from models import Movie
import requests
import json

API_Key = "fc5b36a9efd6644a406776ec36e58170"
def requestlist():
    print('entry to request')
    list_id = '30'
    List_req = f'https://api.themoviedb.org/4/list/{list_id}?page=1&api_key={API_Key}'
    response = requests.get(List_req)
    print(response.text)
    readjson(response.text)
    print('end request call')
    #return response.text

def readjson(stringResponse):
    print('reading Json')
    entites = json.loads(stringResponse)
    entites = entites['results']
    json_array = entites
    results_list = []


    for result in json_array:
        movie_info = {"id": None, "original_language": None, "original_title": None, "overview": None,
                      "popularity": None, "poster_path": None, "release_date": None, "title": None}
        print(result['original_title'])
        movie_info['id'] = result['id']
        movie_info['original_language'] = result['original_language']
        movie_info['original_title'] = result['original_title']
        movie_info['overview'] = result['overview']
        movie_info['popularity'] = result['popularity']
        movie_info['release_date'] = result['release_date']
        movie_info['title'] = result['title']
        results_list.append(movie_info)
        append_database(movie_info)

    query_results = Movie.objects.all()
    context = {'query_results': query_results}
    render("home.html", 'https://api.themoviedb.org/4/list/{list_id}?page=1&api_key={API_Key}', context)

    return results_list

def append_database(movie_item):
    movieobject = Movie()
    movieobject.Movie_id = movie_item['id']
    movieobject.Movie_original_languag = movie_item['original_language']
    movieobject.Movie_original_title = movie_item['original_title']
    movieobject.Movie_overview = movie_item['overview']
    movieobject.Movie_popularity = movie_item['popularity']
    movieobject.Movie_release_date = movie_item['release_date']
    movieobject.Movie_title = movie_item['title']
    movieobject.save()

   # results_list = Movie.objects.all().order_by('id')




# Create your views here.
'''
def index (response):
    return HttpResponse("Hello world, you are at the polls index ")
'''

