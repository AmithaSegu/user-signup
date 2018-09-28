from flask import Flask, request, redirect, render_template
import re
import os
import jinja2

app = Flask(__name__)
app.config['DEBUG'] = True      # displays runtime errors in the browser, too

@app.route("/")
def index():
    #return form
    #return form.format(username='', username_error='', password='', password_error='',verify_password='', veri_password_error='',email='', email_error='')
    return render_template('home_page.html')

#@app.route("/")
#def display_signup_form():
#    return form.format(username='', username_error='', password='', password_error='',verify_password='', veri_password_error='',email='', email_error='')
    #return form.format("")

def input_empty(name):
    if len(name)>0:
        return True
    else:
        return False

def length_validation(name1):
    if (len(name1)>=3 and len(name1)<=20):
        return True
    else:
        return False

def space_validation(name3):
    if ' ' in  name3:
        return False
    else:
        return True

def email_validate(name4):
    #length=len(name4)
    if '@' in name4:
        if '.' in name4:
            #if name4[length-5] == '.':
            return True
        else:
            return False
    else:
        return False

@app.route("/", methods=['POST'])
def login_page():
    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']
    
    username_error=''
    password_error=''
    veri_password_error=''
    email_error=''
    
    if input_empty(username)==False:
        username_error="Feild is empty.Please enter valid data"
    elif length_validation(username)==False:
        username_error="Username should be in the range of 3 to 20 chars"
    elif space_validation(username)==False:
        username_error="Username has spaces. Please remove and re-enter a valid username"
    else:
        username_error=''

    if input_empty(password)==False:
        password_error="Feild is empty.Please enter valid password"
    elif length_validation(password)==False:
        password_error="Password should be in the range of 3 to 20 chars"
    elif space_validation(password)==False:
        password_error="Password has spaces. Please remove and re-enter a valid password"
    else:
        password_error=''
    
    if input_empty(verify_password)==False:
        veri_password_error="Feild is empty.Please enter valid password"
    elif length_validation(verify_password)==False:
        veri_password_error="Password should be in the range of 3 to 20 chars"
    elif space_validation(verify_password)==False:
        veri_password_error="Password has spaces. Please remove and re-enter a valid password"
    else:
        if verify_password==password:
            veri_password_error=''
        else:
            veri_password_error="Password and Verify password do not match. Please re-enter"

    if len(email)>0:
        if length_validation(email)==False:
            email_error="Email should be in the range of 3 to 20 chars"
        elif space_validation(email)==False:
            email_error="Email has spaces. Please remove and re-enter a valid email"
        elif email_validate(email)==False:
            email_error="Email is not valid. Please enter a valid email"
    else:
        email_error=''
    
    if (not password_error and not username_error and not veri_password_error and not email_error):
    #if (password_error=='' and username_error=='' and veri_password_error=='' and email_error==''):
        #return 'success'
        #return redirect('/welcome?username={0}'.format(username))
        return render_template('welcome.html', name=username)
    elif (not password_error and not veri_password_error and not email_error):
        return render_template('home_page.html',username='',email=email,password='',verify_password='',password_error='',veri_password_error='',email_error='',username_error=username_error)
    elif (not password_error and not veri_password_error and not username_error):
        return render_template('home_page.html',username=username,email='',password='',verify_password='',password_error='',veri_password_error='',email_error=email_error,username_error='')
    elif (not username_error and not email_error):
        return render_template('home_page.html',username=username,email=email,password='',verify_password='',password_error=password_error,veri_password_error=veri_password_error,email_error='',username_error='')
    else:
        return render_template('home_page.html',username=username, password=password, verify_password=verify_password, email=email, username_error=username_error,password_error=password_error,veri_password_error=veri_password_error, email_error=email_error)

#@app.route('/welcome')
#def welcome_page():
#    username=request.args.get('username')
#    #return '<h1> WELCOME! {0} </h1>'.format(username)
#    render_template('welcome.html', name=username)

app.run()
