import urllib
import urllib2
import os

def getHtml_nocookie(url):
    f = urllib.urlopen(url)
    html = f.read()
    return html

def getHtml_cookie(url,Cookie):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',Cookie))
    response = opener.open(url)
    html = response.read()
    return html
#get data
def getData():
    url ='https://www.wechall.net/challenge/training/crypto/transposition1/index.php'
    cookie = 'WC=9126606-17486-rAJqjyfRgf9PulDp'
    html = getHtml_cookie(url,cookie)
    vt = html.find('<div class="box_c">')
    data = html[vt+396:vt+669]
    return data

def Transposition(data,key):
    str = ''
    i = 0
    while(i<len(data)):
        str = str + data[i+1]
        str = str + data[i]
        i = i + 2
    return str

data = 'oWdnreuf.lY uoc nar ae dht eemssga eaw yebttrew eh nht eelttre sra enic roertco drre . Ihtni koy uowlu dilekt  oes eoyrup sawsro don:wn flnbmabldr.o'
i = 1
data = getData()
data = data.replace('&nbsp;',' ')
print Transposition(data,10)


