from flask import render_template
from app import app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/service1')
def service1():
    return render_template('services/service1.html')

@app.route('/service2')
def service2():
    return render_template('services/service2.html')

@app.route('/service3')
def service3():
    return render_template('services/service3.html')

@app.route('/service4')
def service4():
    return render_template('services/service4.html')
