import pandas as pd
import numpy as np
import random
from euclid import sim_euclid
from copy import deepcopy
import math
def getRange(func,listing):
    result = []
    for row in listing:
         result.append(func([float(i) for i in row if isinstance(i,str)==False]))
    return result

blogs = pd.read_csv("blogs.csv",sep="\t")
columns_dict = {(key,value) for key,value in enumerate(blogs.keys())}
blog_matrix = blogs.as_matrix()

mins = getRange(min,blog_matrix)
maxs = getRange(max,blog_matrix)
ranges = zip(mins,maxs)

blog_matrix = blog_matrix.T[1:]

def create_centroids(number):
    result = []
    for i in range(number):
        result.append([random.randint(0,row) for row in maxs])
    return result
def findclosest(blog_matrix,centroids):
    centroids_property = {}
    for number,row in enumerate(blog_matrix):
        curr_list = [sim_euclid(row,centr) for centr in centroids]
        index = curr_list.index(min(curr_list))
        centroids_property.setdefault(index,[])
        centroids_property[index].append(number)
    return centroids_property


def vectorSum(vector_one):
    result = deepcopy(vector_one)
    def averager(vector_one):
        for index in range(len(result)):
            result[index]+=vector_one[index]
        return result
    return averager


def getNewCentroids(centrs,blog_matrix):
    newCentroids = []
    for key,value in centrs.items():
        summ=vectorSum(blog_matrix[value[0]])
        newval = [summ(row)/len(row) for index,row in enumerate(blog_matrix) if index in centrs[key]]
        newCentroids.append(newval[0])
    return newCentroids

def difference(arg_one,arg_two):
    result=0
    elements=0
    for index,row in enumerate(arg_two):
        for jndex,col in enumerate(arg_two):
            elements+=1
            result += math.pow(arg_one[index][jndex] - arh_two[index][jndex],2)
    return result/elements


def kmeans(blog_matrix,k):
    centr = create_centroids(k)
    prelast = [0,1]
    last = [1,1]
    while last!=prelast:
        print("stepping")
        prelast = last
        last = findclosest(blog_matrix,centr)
        centr = getNewCentroids(last,blog_matrix)
    return last
