import urllib
import urllib2
import os

def getHtml_nocookie(url):
    f = urllib.urlopen(url)
    html = f.read()
    return html

def addPara(url,values):
    url= url + '/?'
    for key in values.keys():
        url = url + key +'=' + values[key] + '&'
    url.strip('&')
    print url

def getHtml_cookie(url,Cookie):
    opener = urllib2.build_opener()
    opener.addheaders.append(('Cookie',Cookie))
    response = opener.open(url)
    html = response.read()
    return html

def Upload(url,data):
    post = urllib.urlencode(data)
    result_file = open('reslut.html','w')
    response = opener.open(url,post)
    result_file.write( response.read())
    print 'ok'

def saveHtml(html):
    f = open('keke.html','w+')
    for i in html:
        f.write(i)
def showTime(html):
    vt = html.find('<br/>You')
    print html[vt+5:vt+49]

def get(url, cookie):
    request = urllib2.Request(url);
    request.add_header('Cookie',cookie);
    response = urllib2.urlopen(request);
    message = response.read();
    return message

i=0;
cookie = 'WC=9127924-17486-rwTPvFzd48yYKskf'
while i<10:
    url = 'https://www.wechall.net/challenge/training/programming1/index.php?action=request'
    
    html = getHtml_cookie(url,cookie)
    print html

    url = 'https://www.wechall.net/challenge/training/programming1/index.php?answer='+html
    html = getHtml_cookie(url,cookie)
    showTime(html)
    i= i+1

saveHtml(html)

