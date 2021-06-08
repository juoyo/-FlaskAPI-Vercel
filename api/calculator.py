from flask import Flask, Response, request, redirect, url_for
import sympy
from sympy.abc import x, y, z


app = Flask(__name__)

@app.route('/api/calculator',methods = ['POST', 'GET'])
def login():
  if request.method == 'POST':
      cal_para1 = request.form['cal_para1']
  else:
      cal_para1 = request.args.get('cal_para1')

  result = str(eval(cal_para1))
  return  result




