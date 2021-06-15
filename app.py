from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars


app = Flask(__name__)
mongo = PyMongo(app, uri="mongodb://localhost:27017/Mission_to_mars")


@app.route("/")


def home():
    #Find one record from Mongo database
    mars_info = mongo.db.collection.find_one()
    #Return template and data
    return render_template("index.html", mars_info=mars_info)


@app.route('/scrape')


def scrape():
    #Run the scrape function in the scrape_mars file
    mars_data = scrape_mars.scrape_news()
    #Insert data into Mongo database
    mongo.db.collection.update({}, mars_data, upsert=True)
    #Return back to homepage
    return redirect("/")
    
if __name__ == "__main__":
    app.run(debug=True)