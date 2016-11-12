import urllib2
from bs4 import BeautifulSoup
import datetime
import time

url = '''http://pingomatic.com/ping/?title=Teckguide&blogurl=http%3A%2F%2Fteckguide.blogspot.com
%2F&rssurl=http%3A%2F%2Fteckguide.blogspot.com%2Ffeeds%2Fposts%2Fdefault%3Falt%3Drss&chk_weblogscom=on&chk_blogs=
on&chk_feedburner=on&chk_newsgator=on&chk_myyahoo=on&chk_pubsubcom=on&chk_blogdigger=on&chk_weblogalot=on&chk_newsisfree=
on&chk_topicexchange=on&chk_google=on&chk_tailrank=on&chk_skygrid=on&chk_collecta=
on&chk_superfeedr=on&chk_audioweblogs=on&chk_rubhub=on&chk_a2b=on&chk_blogshares=on'''

while True:
    try :
        response = urllib2.urlopen(url.replace('\n','')).read()
    except urllib2.URLError as e:
        msg = 'url error'
        print msg
    soup = BeautifulSoup(response,'html.parser')
    if "pinging complete!" in soup.text.lower():
        msg = 'ping successful'
        print msg
        time.sleep(1800)
    elif 'slow' in soup.text.lower():
        msg = 'too quick'
        print msg
        time.sleep(600)
