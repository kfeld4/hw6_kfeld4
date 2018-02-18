# 507/206 Homework 6 Part 2
import requests
from bs4 import BeautifulSoup


#### Part 2 ####
print('\n*********** PART 2 ***********')
print('Michigan Daily -- MOST READ\n')

html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, "html.parser")

searching_div = soup.find(class_="panel-pane pane-mostread")
#print(searching_div)

finding_most_reads = searching_div.descendants

for x in finding_most_reads:
    if x.name == "a":
        print(x.text)
