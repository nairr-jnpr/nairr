from flask import Flask,render_template,request

app = Flask(__name__)

params = []
headers = ['Label', 'Total Tests', 'Passed', 'Failed']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/json', methods=['POST'])
def json():

    req = request.get_json()
    print(req)
    global params
    global headers
    #params = [req['label'], req['total test'], req['passed'], req['failed']]

    try:
        label = req['label']
    except:
        label = '0.0.0'
    try:
        tot = req['total test']
    except:
        tot = '0'

    try:
        pasd = req['passed']
    except:
        pasd = '0'

    try:
        fails = req['failed']
    except:
        fails = '0'

    params = [label,tot,pasd,fails]

    return "Json posted"


@app.route('/table')
def table():
    if len(params)>0:
        return render_template('table.html',params=params, headers=headers)
    else:
        return render_template('table.html',params=['0.0.0',0,0,0],headers=headers)

if __name__=='__main__':
    app.run(debug=True)