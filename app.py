import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from env import MONGO_URI

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'tater-rater'
app.config["MONGO_URI"] = (MONGO_URI)

mongo = PyMongo(app)

@app.route('/') 
@app.route('/get_potatoes') #will display gallery of potatoes from mongodb
def get_potatoes():
    return render_template("potatoes.html", potatoes=mongo.db.potatoes.find())

@app.route('/add_potato') #opens up the page for submitting a potato
def add_potato():
    return render_template("submit.html")

@app.route('/submit_potato', methods=['POST']) #posts data collected on the submit.html form to mongodb, then redirects to potato gallery
def submit_potato():
    potatoes=mongo.db.potatoes
    potatoes.insert_one(request.form.to_dict())
    return redirect(url_for('get_potatoes'))

@app.route('/profile/<potato_id>')
def profile(potato_id):
    the_potato =  mongo.db.potatoes.find_one({"_id": ObjectId(potato_id)})
    return render_template('profile.html', potato=the_potato)

if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)