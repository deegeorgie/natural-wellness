"""
Routes and views for the flask application.
"""
from datetime import datetime
from flask import render_template
from natural import app
from flask_googlemaps import GoogleMaps
from flask import request
from flask import url_for, redirect
from flask import jsonify

app.config['GOOGLEMAPS_KEY'] = "AIzaSyD6ef9YyPKHwSxsk2s_UdA_Czo1Jiu4flg"
GoogleMaps(app)


from pymongo import MongoClient
uri = 'mongodb://deebodiong:jhlfd1974@ds028540.mlab.com:28540/wellness'
client = MongoClient(uri)
db = client.wellness
contacts = db.contacts


@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Veuillez nous contacter par ce formulaire'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/add_contact', methods=['POST'])
def add_contact():
    try:
        nom = request.values.get('yourname')
        email = request.values.get('youremail')
        telephone = request.values.get('yourphone')
        message = request.values.get('yourmessage')

        contacts.insert({"nom":nom, "email":email, "telephone":telephone, "message":message})
#        return jsonify(status='OK',message='inserted successfully')
        return redirect('/merci/')  
    except Exception,e:
        return jsonify(status='ERROR',message=str(e))
#        return redirect('/merci/')

@app.route('/merci/')
def merci():
    return render_template('merci.html')