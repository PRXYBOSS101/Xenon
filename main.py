import requests
from flask import Flask, request
from rewriter import rewriter
import json 


config = json.load(open('config.json'))

app = Flask(__name__)

@app.route('/')
def main():
    return json.dumps(config, indent=4, sort_keys=True, default=str, ensure_ascii=False)

@app.route(f'/{config["prefix"]}/<path:url>')
def proxy(url):
    header = request.headers
    header = {k: json.dumps(v) if isinstance(v, dict) else v for k,v in header.items()}
    cookies = request.cookies
    del header['Host']
    if "Host" in header:
        del header['Host']
    elif "X-Forwarded-Host" in header:
        del header['X-Forwarded-Host']
    elif "X-Forwarded-Server" in header:
        del header['X-Forwarded-Server']
    elif "X-Forwarded-For" in header:
        del header['X-Forwarded-For']
    elif "X-Forwarded-Proto" in header:
        del header['X-Forwarded-Proto']
    elif "X-Forwarded-Port" in header:
        del header['X-Forwarded-Port']
    elif "X-Forwarded-Path" in header:
        del header['X-Forwarded-Path']
    elif "Sec-Fetch-Site" in header:
        del header['Sec-Fetch-Site']
    elif "Sec-Fetch-Mode" in header:
        del header['Sec-Fetch-Mode']
    elif "Sec-Fetch-Dest" in header:
        del header['Sec-Fetch-Dest']
    elif "Sec-Fetch-User" in header:
        del header['Sec-Fetch-User']
    elif "referer" in header:
        del header['referer']
    elif 'Access-Control-Allow-Origin' in header:
        del header['Access-Control-Allow-Origin']

    del header['Accept-Encoding']

    if url.endswith('.html'):
        header['Content-Type'] = 'text/html'
    elif url.endswith('.css'):
        header['Content-Type'] = 'text/css'
    elif url.endswith('.js'):
        header['Content-Type'] = 'text/javascript'
    

    if url.startswith('http://') or url.startswith('https://'):
        for i in config['blacklist']:
            if i == url:
                return "This site is blacklisted"
            else:
                continue
        r = requests.get(url, headers=header)
        html = r.text
    else:
        url = f'http://{url}'
        for i in config['blacklist']:   
            if i == url:
                return "This site is blacklisted"
            else:
                continue
        r = requests.get(url, headers=header, cookies=cookies)
        html = r.text

    return rewriter(html, config["prefix"], config["domain"], url)


if __name__ == '__main__':
    import bjoern

    bjoern.run(app, host="0.0.0.0", port=int(config['port'])) 