import pandas as pd
from korelationofpirson import sim_pearson
from recomendations import topMatches
rating_by_id = pd.read_csv("ml-latest-small/ratings.csv")
movie_by_id = pd.read_csv("ml-latest-small/movies.csv")

print(str(movie_by_id[movie_by_id["movieId"]==4775]["title"]))
my_map = {}
for index,item in enumerate(rating_by_id["userId"]):
    if item in my_map.keys():
        pass
    else:
        my_map[item]={}
    current_movie = rating_by_id["movieId"][index]
    current_rating = rating_by_id["rating"][index]
    my_map[item][current_movie] = current_rating

def listmerge1(lstlst):
    all=[]
    for lst in lstlst:
        for el in lst:
            all.append(el)
    return all

def findMax(critics):
    recomend_list = []
    for item in critics:
        score,critic = item
        minimap  = my_map[critic]
        minimap  = sorted(minimap, key = minimap.__getitem__)
        minimap.reverse()
        recomend_list.append(minimap[0:5])
    recomend_list = listmerge1(recomend_list)
    return recomend_list

def getMoviesList(id_list):
    return_list = []
    for item in id_list:
        try:
            return_list.append(str(movie_by_id[movie_by_id["movieId"]==int(item)]["title"]))
        except:
            pass
    return return_list
def getResult():
    name = input("Please enter your name")
    my_rate = input("Please enter the film rate(Example: Titanic:4.5,Heroic:5.6)")
    my_list = my_rate.split(",")
    this_map = {}
    for item in my_list:
        key,value = item.split(":")
        value = float(value)
        this_map[key]=value
    my_map[name]=this_map
    best_critic = topMatches(my_map,name,5)
    best_movies = findMax(best_critic)
    result = getMoviesList(best_movies)
    for item in result:
        try:
            print(item)
        except:
            print("helloworld")
getResult()
