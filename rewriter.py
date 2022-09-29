from rewrite.a import aRewrite
from rewrite.iframe import iframeRewrite
from rewrite.img import imgRewrite
from rewrite.link import linkRewrite
from rewrite.script import scriptRewrite
from rewrite.source import sourceRewrite
from rewrite.embed import embedRewrite
from rewrite.base import baseRewrite
from rewrite.audio import audioRewrite
from rewrite.area import areaRewrite
from rewrite.track import trackRewrite
from rewrite.link import linkRewrite
from rewrite.meta import metaRewrite
from bs4 import BeautifulSoup



def rewriter(code, prefix, domain, requestURL):
    


    # html rewriting
    soup = BeautifulSoup(code, 'html.parser')
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
    linkRewrite(prefix, domain, requestURL, soup)
    metaRewrite(prefix, domain, requestURL, soup)
    

    return soup.prettify()
