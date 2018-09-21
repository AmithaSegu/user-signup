from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

form="""
<!DOCTYPE html>
    <html>
        <body>
        <h1>SIGNUP</h1>
        <form>
            <label for="username">Username
                <input type="text", name=username />
            </label><br><br>
            <label for="password">Password
                <input type="password", name=password />
            </label><br><br>
            <label for="verify_password">Verify Password
                <input type="password", name=verify_password />
            </label><br><br>
            <label for="email">Email(optional)
                <input type="text", name=email />
            </label><br><br>
            <input type="submit", value='SUBMIT' />
        </form>
        </body>
    </html>
"""


@app.route("/")
def index():
    return form
app.run()
