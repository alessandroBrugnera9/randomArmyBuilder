from flask import Flask,jsonify,request
import random
from json2html import *

def generateArmy(dic:dict):
    dic=dict( [(k,v) for k,v in dic.items() if v])
    numTroops=dic["num"]
    dic.pop("num")
    typesTroops=len(dic)
    response={}
    min=1
    max=int(numTroops)-typesTroops+1
    iterationDic=list(dic.values())[:-1] #leave last element out to fill the rest the army with this type of troop
    for troop in iterationDic:
        response[troop]=random.randint(min,max)
        max=max-response[troop]+1
    response[list(dic.values())[-1]]=max
    return response

app = Flask(__name__)
@app.route('/api', methods=['GET', 'POST'])
def resp():
    try:
        dic=request.form.to_dict()
        response=generateArmy(dic)
        return jsonify(response), 200
    except:
        return "Something went wrong", 400

@app.route('/api/pretty', methods=['GET', 'POST'])
def resp2():
    try:
        dic=request.form.to_dict()
        response=generateArmy(dic)
        table=json2html.convert(json = response)
        return table, 200
    except:
        return "Something went wrong", 400

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=9090)