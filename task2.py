

from task1 import scrape_data
import json 

screpped=scrape_data()
def scrape_data_1(movie):
    years=[]
    for i in movie:
        year =i["Year"]
        if year not in years:
            years.append(year)
    movie_dic = {i:[]for i in years}
    for i in movie:
        year = i["Year"]
        for x in movie_dic:
            if str(x)==str(year):
                movie_dic[x].append(i)
        with open("task2.json","w") as file:
            json.dump(movie_dic,file,indent=4)
    return movie_dic
scrape_data_1(screpped)


