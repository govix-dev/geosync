from flask import Flask as fk,render_template as rd,redirect as re


app=fk(__name__)

@app.route('/',methods=['POST','GET'])
def start_page():
    return rd('main_page.html')


@app.route('/details',methods=['POST','GET'])
def detail_page():
    return "Work in Progress"


@app.route('/results',methods=['POST','GET'])
def result_page():
    return "Work in Progress"


@app.route('/about',methods=['POST','GET'])
def about_page():
    return "Work in Progress"

@app.route('/admin',methods=['POST','GET'])
def admin_page():
    return "Work in Progress"