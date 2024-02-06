from flask_cors import *
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/data-visualization')
def data_visualization():
    return render_template('data_visualization.html')

@app.route('/regulations')
def regulations():
    return render_template('regulations.html')

@app.route('/public-opinion-analysis')
def public_opinion_analysis():
    return render_template('public_opinion_analysis.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/map')
def show_map():
    return render_template('static/uk_regions_map.html')

@app.route('/2022england')
def index():
    return render_template('2022england.html')

if __name__ == '__main__':
    app.run(debug=True)


