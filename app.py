from flask import Flask, render_template, request
import model

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        if username == 'godlove' and password == 'godlove':
            return render_template('about.html')
        else:
            error_message = 'Crendential not valide'
            return render_template('index.html', message = error_message)

@app.route('/about', methods = ['GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(port=7000, debug=True)