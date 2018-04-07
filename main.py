from flask import Flask, request, render_template, redirect
import cgi
import os

app = Flask(__name__)
app.config['DEBUG']=True


@app.route("/")
def index():
    return render_template('home.html')


@app.route("/home", methods = ['POST'])
def home():
    username = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    verify_error = ''
    email_error = ''

    if len(username) == 0 or len(username) < 3 or len(username) > 20 or ' ' in username:
        username_error = "That's not a valid username" 

    if len(password) == 0 or len(password) < 3 or len(password) > 20 or ' ' in password:
        password_error = "That's not a valid password"

    if len(verify_password)== 0 or verify_password != password: 
        verify_error = "Passwords do not match"
    
    if len(email) > 0:
        if len(email) < 3 or len(email) > 20 or email.count('@') != 1 or email.count('.') != 1:
            email_error = "Not a valid email"
  
        

    if username_error == '' and password_error == '' and verify_error == '' and email_error =='': 
        return redirect ('/welcome?username=' + username)
    
    else:
        return render_template('home.html', username_error=username_error, password_error=password_error, verify_error=verify_error, email_error=email_error, username=username, email=email)


@app.route('/welcome', methods = ['POST', 'GET'])
def welcome():
    username = request.args.get('username')
    return render_template('welcome.html', username=username)

app.run()