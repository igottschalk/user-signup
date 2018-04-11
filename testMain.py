from flask import Flask, request, redirect
import cgi


app = Flask(__name__)
app.config['DEBUG'] = True


signup_form = """
    <style>
        .error {{color: red;}}
    </style>
    <h1>Signup</h1>
    <form method="POST">
        <label for="username">Username
            <input name="username" type="text" value="{username}" />
        </label>
        <p class="error">{username_error}</p>
        <label for="password">Password
            <input name="password" type="password" value="{password}" />
        </label>
        <p class="error">{password_error}</p>
		<label for="verify">Verify Password
            <input name="verify" type="password" value="{verify}" />
        </label>
        <p class="error">{verify_error}</p>
		<label for="email">Email (optional)
            <input name="email" type="email" value="{email}" />
        </label>
        <p class="error">{email_error}</p>
        <input type="submit" value="Validate" />
    </form>
"""

@app.route("/")
def display_signup_form():
    return signup_form.format(username="", username_error="", 
        password="", password_error="", verify="", verify_error="", email="", email_error="")

@app.route("/", methods=['POST'])
def form_values():
	resp = ""
	for field in request.form.keys():
		resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])
	return resp

app.run()