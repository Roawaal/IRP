from flask_cors import *
from flask import Flask,render_template, request, jsonify

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


@app.route('/chart')
def chart():
    return render_template('2010_2022cap.html')


@app.route('/your/flask/endpoint', methods=['POST'])
def process_names():
    data = request.get_json()
    names = data.get('names')
    # Process names as needed
    print("Received names:", names)
    return jsonify({'message': 'Names received successfully'})

if __name__ == '__main__':
    app.run(debug=True)


