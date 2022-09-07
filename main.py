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
    r = requests.get(url)
    html = r.text
    
    return rewriter(html, config["prefix"], config["domain"], url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=config['debug'], port=config['port'])