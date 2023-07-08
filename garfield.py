import requests
from bs4 import BeautifulSoup

blacklist = ["user", "feature", "upload"]
year = 1978
month = 6
day = 19 
no_comic_alert = 0

print("This program will download every Garfield comic that exists. Would you like to continue?   (Y/n)")
confermation = input()
if confermation == "Y" or confermation == "y":
        pass
else:
        exit()

while year != 2024:
        if month == 13:
                month = 1
                year += 1
        if day == 32:
                day = 1
                month +=1
        def getdata(url): 
                r = requests.get(url) 
                return r.text
        htmldata = getdata('https://www.gocomics.com/garfield/' + str(year) + '/' + '0' + str(month) + '/' + str(day) + '/') 
        soup = BeautifulSoup(htmldata, 'html.parser')
        for item in soup.find_all('img'):
                if blacklist[0] not in item['src'] and blacklist[1] not in item['src'] and blacklist[2] not in item['src']:
                        no_comic_alert = 1
                        print()
                        print(str(day) + "/" + str(month) + "/" + str(year) + ": Downloading")
                        print()
                        url = item['src']
                        response = requests.get(url)
                        with open(str(day) + "_" + str(month) + "_" + str(year) + '.png', 'wb') as f:
                                f.write(response.content)
        if no_comic_alert == 0:
                print()
                print(str(day) + "/" + str(month) + "/" + str(year) + ": No Comic")
                print()
        day += 1
        no_comic_alert = 0

print("All comics have been downloaded. Strike enter to exit.")
input()
