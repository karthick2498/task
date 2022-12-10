from flask import Flask, request
from flask import render_template
import cx_Oracle as ox
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html',data=0)

@app.route('/submit',methods=['POST','GET'])
def validate():
    name = request.form['name']
    jobrole = request.form['currdes']
    currexp = request.form['currexp']
    pastexp = request.form['pastexp']
    skillList  = request.form.getlist('skills')
    techList = request.form.getlist('tech')
    skillCount = skillList.count('1')
    techCount = techList.count('1')
    exp = int(pastexp)+int(currexp)
    data = 0
    if((math.ceil((techCount/6)*100)>=70) and math.ceil((skillCount/4)*100) and (exp >= 4 and exp<= 11)):
        try:
            conn = ox.connect('task1/admin123@127.0.0.1/xe')
            cur = conn.cursor()
            sql = "insert into elg1(name,exp,jobrole) values("+"'"+str(name)+"'"+","+str(exp)+","+"'"+str(jobrole)+"'"+")"
            print(sql)
            cur.execute(sql)
            conn.commit()
            conn.close()
            data = 1
        except:
            data = 2
    else:
        data=-1
        
    return render_template('form.html',data = [data])
