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
    url ='https://www.wechall.net/challenge/training/crypto/caesar2/index.php'
    cookie = 'WC=9124328-17486-0bXTKlxsNmvR4MqL'
    html = getHtml_cookie(url,cookie)
    vt = html.find('<pre style="font-family: monospace;">')
    data = html[vt+37:vt+773]
    return data

def H2ASCII(data):
    str = data.split(' ')
    print str
    out = ''
    for i in str:
        out = out + chr(int(i,16))
    return out

def Caesar(data,x):
    
    str = ''
    i = 0
    while i < len(data):
        if(data[i] == ' '):
            str = str + data[i]
            i = i+1
        else:
            vt = (ord(data[i])+x)%128
            str = str + chr(vt)
            i=i+1
    if(str.find('solution')>=0):
        print str
        return 1
    else:
        return 0



data = '?gg\ bgZ$ qgm kgdn]\ gf] egj] [`Ydd]f_] af qgmj bgmjf]q& L`ak gf] oYk ^Yajdq ]Ykq lg [jY[c& OYkfl al7 )*0 c]qk ak Y imal] keYdd c]qkhY[]$ kg al k`gmd\fl `Yn] lYc]f qgm lgg dgf_ lg \][jqhl l`ak e]kkY_]& O]dd \gf]$ qgmj kgdmlagf ak ]]h]dkhgZ\ka&'
hex_str = '1A 42 42 37 20 3D 42 35 7F 20 4C 42 48 20 46 42 3F 49 38 37 20 42 41 38 20 40 42 45 38 20 36 3B 34 3F 3F 38 41 3A 38 20 3C 41 20 4C 42 48 45 20 3D 42 48 45 41 38 4C 01 20 27 3B 3C 46 20 42 41 38 20 4A 34 46 20 39 34 3C 45 3F 4C 20 38 34 46 4C 20 47 42 20 36 45 34 36 3E 01 20 2A 34 46 41 7A 47 20 3C 47 12 20 04 05 0B 20 3E 38 4C 46 20 3C 46 20 34 20 44 48 3C 47 38 20 46 40 34 3F 3F 20 3E 38 4C 46 43 34 36 38 7F 20 46 42 20 3C 47 20 46 3B 42 48 3F 37 41 7A 47 20 3B 34 49 38 20 47 34 3E 38 41 20 4C 42 48 20 47 42 42 20 3F 42 41 3A 20 47 42 20 37 38 36 45 4C 43 47 20 47 3B 3C 46 20 40 38 46 46 34 3A 38 01 20 2A 38 3F 3F 20 37 42 41 38 7F 20 4C 42 48 45 20 46 42 3F 48 47 3C 42 41 20 3C 46 20 38 38 43 38 3F 46 43 42 35 37 46 3C 01'
i = 1;
data = getData()
data = H2ASCII(hex_str)
while i <= 127 and Caesar(data,i)==0:
    i = i +1

