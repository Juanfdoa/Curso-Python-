from flask import Flask, render_template

# Create Flask App
app = Flask(__name__)

# Define Route
@app.route("/")
def home():
    return render_template('index.html')

# Gretting Route
@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)

# About Route
@app.route('/about')
def about():
    return render_template('about.html')

# 404 Route
@app.errorhandler(404)
def error404(error):
    return render_template('error404.html'), 404

# Run App
if __name__ == "__main__":
    app.run(debug=True)