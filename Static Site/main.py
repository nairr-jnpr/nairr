from flask import Flask,render_template,request

app = Flask(__name__)

params = []
headers=['Label','Total Tests','Passed']
rows = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/json', methods=['POST'])
def json():
    global rows
    rows = []
    req = request.get_json()
    for label in req['labels']:
        row = [label['label'],label['total_test'],label['passed']]
        #print(row)
        rows.append(row)

    return 'Json posted'


@app.route('/overview')
def overview():
    return render_template('overview.html',rows=rows,headers=headers)

if __name__=='__main__':
    app.run(debug=True)
