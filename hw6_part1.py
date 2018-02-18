
# 507/206 Homework 6 Part 1
import requests
from bs4 import BeautifulSoup

#### Part 1 ####
print('\n*********** PART 1 ***********')
print("Mark's page -- Alt tags\n")


html = requests.get("http://newmantaylor.com/gallery.html").text
soup = BeautifulSoup(html, 'html.parser')

searching_img = soup.find_all("img")
#print(searching_img)

for x in searching_img:
    if "alt" in x.attrs:
        print(x["alt"])
    else:
        print("No alternative text provided!")
