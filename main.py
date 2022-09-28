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
    if url.startswith('http://') or url.startswith('https://'):
        for i in config['blacklist']:
            if i == url:
                return "This site is blacklisted"
            else:
                continue
        r = requests.get(url)
        html = r.text
    else:
        url = f'http://{url}'
        for i in config['blacklist']:
            if i == url:
                return "This site is blacklisted"
            else:
                continue
        r = requests.get(url)
        html = r.text

    return rewriter(html, config["prefix"], config["domain"], url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=config['debug'], port=config['port']) 