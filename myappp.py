from flask import *
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacts')
def contact():
    return render_template('contacts.html')

@app.route('/foo/<name>')
def foo(name):
    return render_template('index.html', to=name)

@app.route('/whereami')
def whereami():
    return 'Ghana!'

if __name__ == '__main__':
    port = os.environ.get('PORT',5000)
    app.run(debug=True, host='0.0.0.0',port=port)
    

