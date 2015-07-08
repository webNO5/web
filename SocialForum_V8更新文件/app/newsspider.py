import urllib2
import re

class new:
    def __init__(self):
        self.url='http://tech.baidu.com'

    def run(self):
        result=[]
        page=urllib2.urlopen(self.url)
        content=page.read()
        href=re.findall('<li><a href=".+" mon=".+" target="_blank">[^<].+</a></li>',content)
        for h in href:
            try:
                result.append({'url':h[h.index('href=')+6:h.index('" mon="')],'title':h[h.index('target="_blank">')+16:h.index('</a></li>')].decode('gb2312')})
            except Exception,e:
                pass
        return result


