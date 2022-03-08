from flask import Flask,request,redirect,url_for,render_template,jsonify
import requests
import json

app = Flask(__name__)
#app.jinja_env.filters['zip'] = zip
headers = ['Name','Login','Created At','Updated At','Url']
params=[]
@app.route('/')
def home():
    global params
    url = 'https://api.github.com/users/Rahul-Nair99'
    resp = requests.get(url)
    js = json.loads(resp.text)
    print(js)
    name = js['name']
    login = js['login']
    crtat = js['created_at']
    updat = js['updated_at']
    purl = js['url']
    params = [name,login,crtat,updat,purl]
    return redirect(url_for('table'))

@app.route('/table')
def table():
    if len(params)>0:
        return render_template('profile.html',headers=headers, params=params,zip=zip)
    else:
        return render_template('profile.html',headers=headers,params=['name','login','crtat','updat','purl'])

if __name__=='__main__':
    app.run(debug=True)