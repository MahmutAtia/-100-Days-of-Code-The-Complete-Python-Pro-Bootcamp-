import requests
from bs4 import BeautifulSoup


response = requests.get(url="https://news.ycombinator.com/", )
html = response.text

soup  = BeautifulSoup(html, "html.parser")
titles = soup.find_all("a", class_= "titlelink")




'''----------------------------------------------- 100 Films ---------------------------------'''

film_response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
film_soup = BeautifulSoup(film_response.text, "html.parser")
titles = film_soup.find_all(name="h3", class_= "title")
# i = 1
# for title in titles:
#      t = title.text
#
#      s = t.split(")")
#
#
#      try:
#       print(f"{i}" + s[1])
#      except:
#          s = t.split(":")
#          print(f"{i}" + s[1])
#      i+=1

list = [title.text for title in titles]
print(list[::-1])