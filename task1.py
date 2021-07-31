# from bs4 import BeautifulSoup
# import requests
# import json
# def scrap_data():
#     url="https://www.imdb.com/india/top-rated-indian-movies/"
#     api=requests.get(url)
#     # print(api)
#     htmlparser=api.content
#     # print(htmlparser)
#     soup=BeautifulSoup(htmlparser,"html.parser")
#     # print(soup)
#     div=soup.find("div",class_="lister")
#     # print(div)
#     main_div=div.find("tbody",class_="lister-list")
#     # print(main_div)
#     tr = main_div.find_all("tr")
#     # print(tr)
#     a=[]
#     var=0
#     for i in tr:
#         var=var+1
#         movie_name=i.find("td",class_="titleColumn").a.get_text()
#         # print(movie_name)
#         # a.append(movie_name)
#         name_1=movie_name
#         year=i.find("td",class_="titleColumn").span.get_text()[1:5]
#         # a.append(year)
#         # print(year)
#         year_1=year
#         rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
#         # print(rating)
#         rating1=rating
#         url=i.find("td",class_="posterColumn").a["href"]
#         # print(url)
#         url1="https://www.imdb.com"+url

#         position={"position":var,"movie_name":name_1,"movie_year":year_1,"movie_rating":rating1,"movie_url":url1}
#         a.append(position)
#         with open("movies_data.json","w")as f:
#             json.dump(a,f,indent=4)
#     return(a)
# scrap_data()


import requests
import json
from bs4 import BeautifulSoup
# import pprint


def scrape_data():
    url = "https://www.imdb.com/india/top-rated-indian-movies/"
    page = requests.get(url)
    htmlc=page.content
    soup = BeautifulSoup(htmlc,"html.parser")
    div=soup.find("div",class_="lister")
    s=div.find("tbody",class_="lister-list")
    name=s.find_all("tr")
    top_movie=[]
    searial_number=1
    for i in name:
        details={}
        movie_name=i.find("td",class_="titleColumn").a.get_text()
        year=i.find("td",class_="titleColumn").span.get_text()
        rating=i.find("td",class_="ratingColumn imdbRating").strong.get_text()
        url=i.find("td",class_="titleColumn").a["href"]
        movie_url="https://www.imdb.com"+url
        details={"Position":searial_number,"Name":movie_name,"Year":int(year[1:5]),"Rating":float(rating),"URL":movie_url}
        searial_number+=1
        top_movie.append(details)
        with open("task_1.json","w") as file:
            json.dump(top_movie,file,indent=2)
    return top_movie

scrape_data()


    