from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.appiontment import appiontment



@app.route('/appointment/add')
def add_appiontment():
    return render_template('add_appiontment.html')

@app.route('/appiontments/create',methods=['post'])
def create_appiontment():

    if not appiontment.validate_appiontment(request.form):
        return redirect('/appointment/add')  

    data= {
        'task': request.form['task'],
        'date': request.form['date'],
        'status': request.form['status'],
        'user_id': session['logged_user']
    }

    new_appiontment_id = appiontment.save(data)
    return redirect('/appiontment')