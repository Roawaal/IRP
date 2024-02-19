from flask_cors import *
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def home():
    dynamic_content = "This is dynamic content"
    return render_template('home.html', content=dynamic_content)

@app.route('/data-visualization')
def data_visualization():
    dynamic_content = "This is dynamic content"
    return render_template('data_visualization.html', content=dynamic_content)

@app.route('/regulations')
def regulations():
    dynamic_content = "This is dynamic content"
    return render_template('regulations.html', content=dynamic_content)

@app.route('/public-opinion-analysis')
def public_opinion_analysis():
    dynamic_content = "This is dynamic content"
    return render_template('public_opinion_analysis.html', content=dynamic_content)

@app.route('/contact')
def contact():
    dynamic_content = "This is dynamic content"
    return render_template('contact.html', content=dynamic_content)

@app.route('/map')
def show_map():
    return render_template('static/uk_regions_map.html')



if __name__ == '__main__':
    app.run(debug=True)


