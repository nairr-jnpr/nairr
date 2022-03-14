from flask import Flask,render_template,request

app = Flask(__name__)

headers=['Label','Total Tests','Passed']
rows = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/json', methods=['POST'])
def json():
    global rows
    rows = {}
    req = request.get_json()
    for row in req['labels']:
        rows[row['label']] = {'total_test':row['total_test'],
                              'passed':row['passed'],
                              'failed':row['failed'],
                              'logs':row['logs']
                              }
    return 'Json posted'


@app.route('/overview')
def overview():
    return render_template('overview.html',rows=rows,headers=headers)

@app.route('/details/<label>')
def details(label):
    params = [label,rows[label]['total_test'],rows[label]['passed'],rows[label]['failed'],rows[label]['logs']]
    return render_template('table.html',Label=label,params=params)

if __name__=='__main__':
    app.run(debug=True)
