from flask import Flask, render_template, request, session, redirect, g, url_for
import model

app = Flask(__name__)
app.secret_key = 'my-SECRET_key'

username = ''
user = model.check_users()


@app.route('/', methods=['GET'])
def home():
    return render_template('signin.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session.pop('username', None)
        areyouuser = request.form['username']
        pwd = model.check_pwd(areyouuser)
        if request.form['password'] == pwd:
            session['username'] = request.form['username']
            return redirect(url_for('about'))
    return render_template('signin.html')


'''if request.method == 'GET':
        return render_template('index.html')
    else:
        username = request.form['username']
        password = request.form['password']
        db_password = model.check_pwd(username)
        if password == db_password:
            message = model.show_age(username)
            return render_template('index.html', message = message)
        else:
            error_message = 'Crendential not valide'
            return render_template('index.html', message = error_message) '''


@app.before_request
def before_request():
    g.username = None
    if 'username' in session:
        g.username = session['username']


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        message = "please sign up"
        return render_template('signup.html', message=message)
    else:
        username = request.form["username"]
        password = request.form["password"]
        age = request.form["age"]
        message = model.signup(username, password, age)
        return render_template("signup.html", message=message)


@app.route('/getsession')
def getsession():
    if 'username' in session:
        return session['username']
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')


@app.route('/terms of use', methods=['GET'])
def term_of_use():
    return render_template('term_of_use.html')


@app.route('/privacy', methods=['GET'])
def privacy():
    return render_template('privacy.html')


if __name__ == '__main__':
    app.run(port=7000, debug=True,)
