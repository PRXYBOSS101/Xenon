from rewrite.a import aRewrite
from rewrite.iframe import iframeRewrite
from rewrite.img import imgRewrite
from rewrite.script import scriptRewrite
from rewrite.source import sourceRewrite
from rewrite.embed import embedRewrite
from rewrite.base import baseRewrite
from rewrite.audio import audioRewrite
from rewrite.area import areaRewrite
from rewrite.track import trackRewrite
from bs4 import BeautifulSoup

def rewriter(html, prefix, domain, requestURL):
    soup = BeautifulSoup(html, 'html.parser')
    aRewrite(prefix, domain, requestURL, soup)
    iframeRewrite(prefix, domain, requestURL, soup)
    imgRewrite(prefix, domain, requestURL, soup)
    scriptRewrite(prefix, domain, requestURL, soup)
    sourceRewrite(prefix, domain, requestURL, soup)
    embedRewrite(prefix, domain, requestURL, soup)
    baseRewrite(prefix, domain, requestURL, soup)
    audioRewrite(prefix, domain, requestURL, soup)
    areaRewrite(prefix, domain, requestURL, soup)
    trackRewrite(prefix, domain, requestURL, soup)
    

    return soup.prettify()
