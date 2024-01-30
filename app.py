from flask import Flask, render_template

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
    # Define colors for each region, e.g., {'Scotland': 'red', 'Wales': 'blue'}
    region_colors = {'Scotland': '#ff0000', 'Wales': '#0000ff'}
    return render_template('uk_regions_map.html', region_colors=region_colors)


if __name__ == '__main__':
    app.run(debug=True)
app = Flask(__name__)

