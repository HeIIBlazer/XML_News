import requests
from bs4 import BeautifulSoup
import webbrowser
import ast


url = 'https://www.postimees.ee/rss'

xml_data = requests.get(url).content
soup = BeautifulSoup(xml_data, "xml")

items =soup.find_all("item")
pic=soup.find_all("image")

f=open('helloworld.html','w',encoding='utf-16')

message='''<html>
<head>
<title>Postemees</title>
</head>

<body>
<h1>Postimees</h1>
'''
for item in items[:5]:
    title =item.find('title').text
    message+=f"<h2>{title}</h2>"
    desc=item.find('description').text
    message+=f"<p>{desc}</p>"
    img=item.find('enclosure')['url']
    message+=f"<img src=\"{img}\">"



message += """
</body>

</html>"""
print(message)
f.write(message)
f.close()

webbrowser.open_new_tab('helloworld.html')

    # <h2>Ohtlik värk! Närvimürgiga voodilina on netirahva muigama pannud</h2>
    # <p>Näpuviga tõlkes pakub netirahvale palju kõneainet. Vaatame, millised teooriad seoses sellega tekkinud on!</p>
    # <p>https://pmo.ee/7495998</p>
    # <p>pm#7495998</p>
    # <p>Tue, 12 Apr 2022 08:38:00 +0300</p>
    # <p>Kodu.postimees.ee</p>
    # <p>Kodu</p>