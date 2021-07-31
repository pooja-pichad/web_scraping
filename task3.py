
from task1 import scrape_data
from task2 import scrape_data_1
# # from bs4 import BeautifulSoup
import json


scrapped_data=scrape_data()
movie_by_year=scrape_data_1(scrapped_data)
def scrape_data_2(movie):
    moviedec={}
    list1=[]
    for year in movie:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    # print(list1)
    for i in list1:
        moviedec[i]=[]
    for i in moviedec:
        dec10=i+9
        for x in movie:
            if x<=dec10 and x>=i:
                for v in movie[x]:
                    moviedec[i].append(v)
        with open("task_3.json","w")as file:
            json.dump(moviedec,file,indent=4)
    return moviedec

scrape_data_2(movie_by_year)