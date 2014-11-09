import requests
from alchemyapi import AlchemyAPI
import json

def getNews(query):
    query = str(query)
    f = open('test.html', 'w')
    
    r = requests.get('https://api.datamarket.azure.com/Data.ashx/Bing/Search/News?Query=%27'+ query+'%27maryland%27&$format=json', auth=('Ql9qEoqZut7Uy3i7mTtiX8Dv1SciVZf1Qwcz07BUx5k','Ql9qEoqZut7Uy3i7mTtiX8Dv1SciVZf1Qwcz07BUx5k'))
    rrr = r.json()
    rr = rrr['d']['results']
    length = len(rr)
    alchemyapi = AlchemyAPI()
    
    lurl = []
    linfo = []
    lscore = []
    ltitle = []
    ldesc = []
    
    for i in range(0, length-1):
        lurl.append(rr[i]['Url'])
        ltitle.append(rr[i]['Title'])
        ldesc.append(rr[i]['Description'])
    
    total = 0.0;
    
    for i in range(0, length-1):
        try:
            linfo.append(alchemyapi.sentiment('text', rr[i]['Title'])['docSentiment'])
            if linfo[i]['type'] != 'neutral':
                total += float(linfo[i]['score'])
        except:
            continue
    avg = total/length
    html = '<html> <body>'
    for i in range(0, length-1):
        try:
            html += '<div class="grid-50 mobile-grid-95" width="50%%"> <a href="' + str(lurl[i]) + '">' + str(ltitle[i]) +'</a><br>' + str(ldesc[i]) + '<br></div><br>'
        except:
            continue
    html+= "</body></html>"
    
    return avg, html




