__author__ = 'yfsanchez'

from bs4 import BeautifulSoup
import requests
URL = "https://coinmarketcap.com/"
URL2 = "http://jarroba.com/"

req = requests.get(URL)

status_code = req.status_code
if status_code == 200:
    html = BeautifulSoup(req.text, "lxml")
    entradas = html.find_all('tr')
    for i, entrada in enumerate(entradas):
        if i != 0:
            titulo = entrada.find('td', {'class': "text-center"}).getText()
            print ('%d - %s ' % (i + 1, titulo))
#         titulo = entrada.find('span', {'class': 'tituloPost'}).getText()
#         autor = entrada.find('span', {'class': 'autor'})
#         fecha = entrada.find('span', {'class': 'fecha'}).getText()
#         print ('%d - %s  |  %s  |  %s' % (i + 1, titulo, autor, fecha))
else:
    print ("Status Code %d" % status_code)