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
def Caesar(data,x):
    alpha = {'A':0,'B':1,'C':2,'D':3,'E':4,'F':5,'G':6,'H':7,'I':8,'J':9,'K':10,'L':11,'M':12,'N':13,'O':14,'P':15,'Q':16,'R':17,'S':18,'T':19,'U':20,'V':21,'W':22,'X':23,'Y':24,'Z':25}
    ch = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    str = ''
    i = 0
    while i < len(data):
        if(data[i] == ' '):
            str = str + data[i]
            i = i+1
        else:
            vt = (alpha[data[i]]+x)%26
            str = str + ch[vt]
            i=i+1
    if(str.find('SOLUTION')>=0):
        print str
        return 1
    else:
        return 0

#get data
def getData():
    url ='https://www.wechall.net/challenge/training/crypto/caesar/index.php'
    cookie = 'WC=9123962-17486-XAlvBXWt1EJIRkn1'
    html = getHtml_cookie(url,cookie)
    vt = html.find('<div class="box_c">')
    data = html[vt+20:]

    vt = data.find('<div class="box_c">')
    data = data[vt+19:vt+113]
    return data

data = getData()

i = 1;
while i <= 25 and Caesar(data,i)==0:
    i = i +1

    
