import urllib
from bs4 import BeautifulSoup
html = urllib.request.urlopen('https://ssnanonymus.se.qlikcloud.com/sense/app/aad2fecd-c702-4cb0-8cd6-a570243b4a4f/sheet/rjkqGs/state/analysis')
soup = BeautifulSoup(html) # tranforma el html a un objeto de beautifulSoup
tags = soup('a') # nos trae todas la etiqueta de tipo a href hiperviculos.
