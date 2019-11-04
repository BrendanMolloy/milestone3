import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from env import MONGO_URI



app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'tater-rater'
app.config["MONGO_URI"] = MONGO_URI

mongo = PyMongo(app)

@app.route('/')
@app.route('/get_potatoes')
def get_potatoes():
    return render_template("potatoes.html", potatoes=mongo.db.potatoes.find())


if __name__ == '__main__':
    app.run(host=os.getenv("IP", "0.0.0.0"),
        port=int(os.getenv("PORT", "5000")), debug=True)