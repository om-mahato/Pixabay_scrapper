import urllib.request
from urllib.request import urlretrieve
import urllib.parse
import time

from bs4 import BeautifulSoup

try:
    for page in range(1, 5):
        url='https://pixabay.com/en/photos/?&pagi='+str(page)
        #url_category = 'https://pixabay.com/en/photos/?cat=computer&pagi=2'

        headers = {}
        headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
        req = urllib.request.Request(url, headers = headers)
        resp = urllib.request.urlopen(req)
        print("connection ok")
        respData = resp.read()
        resp.close()
        print('Done')
        soup = BeautifulSoup(respData, "html.parser")
        
        for i in range(0,15):
            image_src = soup.find_all('div',{'class':'item'})
            img = image_src[i].find_all('img')
            print(img)
            image_link = img[0].get('src')
            #print(image_link)
            name = image_link.rsplit('/',1)[-1]
            
            #download the image
            try:
                urlretrieve(image_link, name)
                print('Downloaded image of ' + name)
            except Exception as ee:
                print(str(ee))
                pass
except Exception as e:
    print(str(e))
    