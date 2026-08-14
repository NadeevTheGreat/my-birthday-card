from flask import Flask, render_template

# Configured Flask to look in current folder '.' for templates & static files
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/card')
def card():
    return render_template('card.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)