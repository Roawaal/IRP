from flask import Flask,render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    dynamic_content = "This is dynamic content"
    return render_template('home.html', content=dynamic_content)

@app.route('/map')
def chart():
    return render_template('4_map.html')

@app.route('/event')
def event():
    return render_template('2_events.html')

if __name__ == '__main__':
    app.run()