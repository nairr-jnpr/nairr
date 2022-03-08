from flask import Flask,render_template,jsonify
import requests
import json
from unicodedata import normalize

app = Flask(__name__)

@app.route('/')
def home():
    user = "mistsys"
    token = "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"
    repo = "apfw"
    url = "https://api.github.com/repos/{}/{}/tags".format(user,repo)
    #url = "https://github.com/mistsys/apfw/tags"
    headers = {
        'authorization': 'token {}'.format(token)
    }
    r = requests.get(url,headers=headers)

    str = r.text.encode('ascii','ignore')
    #print(str)
    js = json.loads(str)
    print(type(js))
    for tag in js:
        print(type(tag))
        print(tag['name'])
    print(type(jsonify(js)))
    return jsonify(js)



if __name__ == '__main__':
    app.run(debug=True)

