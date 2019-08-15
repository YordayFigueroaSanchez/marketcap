import urllib.request
from datetime import datetime

now = datetime.now()
fecha = now.strftime("%Y%m%d%H%M%S")
print("fecha:", fecha)

url = 'https://coinmarketcap.com/'
archivo_tmp, header = urllib.request.urlretrieve(url)
with open('dataHTML\\'+'marketcap-'+fecha+'.html', 'wb') as archivo:
    with open(archivo_tmp, 'rb') as tmp:
        archivo.write(tmp.read())