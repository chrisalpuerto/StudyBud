# main flask file
# chris alpuerto

from flask import Flask, request,render_template,app
from yelpapi import YelpAPI
import time, datetime
import os
from dotenv import load_dotenv


app = Flask(__name__, template_folder='../templates',static='../static')
load_dotenv(dotenv_path='hidden.env')
api_key = os.getenv('YELP_API_KEY')
yelp_api = YelpAPI(api_key)


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        location = request.form['location']
        acompany = request.form['acompany']


    return render_template('index.html')
@app.route('/results', methods=['GET', 'POST'])
def results():
    print()

    return render_template('results.html')
@app.route('/about', methods=['GET','POST'])
def about():
    return render_template('about.html')
if __name__ == '__main__':
    app.run(debug=True)