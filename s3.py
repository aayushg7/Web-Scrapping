from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as ureq
from googlesearch import search
myurl = 'https://blockchain-expo.com/europe/speakers/'
l = []
uclient = ureq(myurl)
pghtml = uclient.read()
uclient.close()
page_soup = soup(pghtml,"html.parser")
containers = page_soup.findAll("div", {"class":"speaker-key-details-expand"})
print(len(containers))

filename="speaker2.csv"
f=open(filename,"w")
headers="Event name,Speaker Name,Designation,Company,social media link\n"
f.write(headers)
for i in range(len(containers)):
    name = containers[i].find("h3").get_text()
    desig = containers[i].findAll("h4")[0].get_text().replace(',','')
    comp = containers[i].findAll("h4")[1].get_text().replace(',','')
    query = name + " "  + desig + " " + comp
    for j in search(query, tld="co.in", num=1, stop=1, pause=2):
        social = j
    f.write("Blockchain expo" + "," + name + "," + desig + "," + comp + "," + social + "\n")
    print(social)
f.close()
print("success")
#The event selected was id04 blockchain expo, this script performs scraping of name designation and company
#of the speaker then it uses these three(in that order) and performs a google search and stores the first google search result
# it then writes all the four(name,designation,company,social media link to the .csv file
#I can do more specific things like making separte colomns for facebook,linkedin twitter by making some changes in the script.




    


