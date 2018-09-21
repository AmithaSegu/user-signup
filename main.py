from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form="""
<!DOCTYPE html>
    <html>
        <style>
        .text_box{
            margin: 10px 0 ;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }
        </style>
        <body>
        <h1>SIGNUP</h1>
        <form>
            <label class=text_box for="username">Username
                <input type="text", name="username" />
            </label><br><br>
            <label class=text_box for="password">Password
                <input type="password", name="password" />
            </label><br><br>
            <label class=text_box for="verify_password">Verify Password
                <input type="password", name="verify_password" />
            </label><br><br>
            <label class=text_box   for="email">Email(optional)
                <input type="text", name="email" />
            </label><br><br>
            <input type="submit", value='SUBMIT' />
        </form>
        </body>
    </html>
"""
def input_empty():
    if len(username)<1:
        return False
    elif len(password)<1:
        return False
    elif len(verify_password)<1:
        return False
    else:
        return True

def login_page():
    username=request.form['username']
    password=request.form['password']
    verify_password=request.form['verify_password']
    email=request.form['email']
    

@app.route("/")
def index():
    return form


app.run()
