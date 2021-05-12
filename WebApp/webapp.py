
import sys
sys.path.insert(0, "c:/Users/shafiqah/PycharmProjects/env/")

import pandas as pd
from flask import Flask, request, render_template


dbLocation = 'c:/Users/shafiqah/PycharmProjects/message-collector/jc4.json'
df = pd.read_json(dbLocation)

print('this is from webapp')

def timeConverter(time):

    return time

app = Flask(__name__)



@app.route("/")
def mainpage():
    return 'render_template(index.html) is not working' #render_template('index.html')



# http://192.168.0.11:8080/message/<id> returns bleMessage
@app.route('/message/<int:id>')
def message(id):
    return df.iloc[id][0]


#returns total number of records of messages
@app.route('/allmessages')
def allmessages():

    value = df.size
    return "number of records = "+str(value)


@app.route("/test")
def test():
    return str(df.iloc[2][0].keys())

@app.route("/rtc")
def rtc():
    return df.iloc[2][0].get('rtc')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)