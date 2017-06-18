from flask import Flask, request, redirect, render_template
import os
import jinja2

app = Flask(__name__)
app.debug = True;

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)

@app.route('/signup', methods = ['POST', 'GET'])
def index():

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        verify = request.form['verify']
        email = request.form['email']
        emailerror = ''
        usererror = ''
        passerror = ''
        verifyerror = ''

        if email:
            if '@' not in email or '.' not in email or email.count('@') > 1 or email.count('.') > 1 or len(email) < 3 or len(email) > 20 or ' ' in email:
                emailerror = "That is an invalid email"

        if not username or len(username) < 3 or len(username) > 20 or ' ' in username:
            usererror = "That's not a valid username"

        if not password or len(password) < 3 or len(password) > 20 or ' ' in password:
            passerror = "That's not a valid password"

        if not verify or verify != password:
            verifyerror = "Passwords do not match"

        if not emailerror and not usererror and not passerror and not verifyerror:
            return redirect('/welcome?username={0}'.format(username))
        else:
            return render_template('signup.html', username = username,
            email = email, emailerror = emailerror, usererror = usererror,
            passerror = passerror, verifyerror = verifyerror)

    return render_template('signup.html')

@app.route('/welcome')
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username = username)

app.run()
