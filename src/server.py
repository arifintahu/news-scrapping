from flask import Flask, jsonify
from scrapper import Scrapper
app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello!'

@app.route('/headline')
def headline():
	scrap1 = Scrapper("https://www.cnnindonesia.com/nasional")
	headline = scrap1.getHeadline()
	return jsonify(result = headline)

@app.route('/news')
def news():
	scrap1 = Scrapper("https://www.cnnindonesia.com/nasional")
	article = scrap1.getTitle()
	return jsonify(result = article)
