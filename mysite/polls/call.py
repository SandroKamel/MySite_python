import requests
import json
import os

from models import Movie



API_Key = "fc5b36a9efd6644a406776ec36e58170"
def requestlist(listID):
    print('entry to request')
    list_id = listID
    List_req = f'https://api.themoviedb.org/4/list/{list_id}?page=1&api_key={API_Key}'
    response = requests.get(List_req)
    print(response.text)
    print('end request call')
    return response.text

def readjson(stringResponse):
    print('reading Json')
    entites = json.loads(stringResponse)
    entites = entites['results']
    json_array = entites
    results_list = []


    for result in json_array:
        movie_info = {"title": None, "id": None}
        print(result['original_title'])
        movie_info['title'] = result['original_title']
        movie_info['id'] = result['id']
        results_list.append(movie_info)

    print(results_list)

   # print(entites["results"])
    print("end of reading")




responseJson =requestlist('30')
print(responseJson)
readjson(responseJson)
