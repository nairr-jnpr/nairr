from flask import Flask,render_template,jsonify,redirect,url_for
import requests
import json

app = Flask(__name__)

headers = ['Name','Zipball Url','Tarball Url']
rows=[]

@app.route('/')
def home():
    token = "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"
    user = "mistsys"
    repo = "apfw"
    url = "https://api.github.com/repos/{}/{}/tags".format(user,repo)
    #url = "https://github.com/mistsys/apfw/tags"

    headers = {
        'authorization': 'token {}'.format(token)
    }

    r = requests.get(url,headers=headers)

    js = r.json()

    for tag in js:
        #print(type(tag))
        #print(tag['name']+' '+tag['zipball_url'])
        print(tag)
        row = []
        row.append(tag['name'])
        row.append(tag['zipball_url'])
        row.append(tag['tarball_url'])
        rows.append(row)

    #return jsonify(js)
    return redirect(url_for('table'))

@app.route('/table')
def table():
    return render_template('index.html',headers=headers,rows=rows)


if __name__ == '__main__':
    app.run(debug=True)



