from flask import Flask, request

app = Flask(__name__)

app.config['DEBUG'] = True


form = """
<!DOCTYPE html>
<html>
    <head> 
        <title>Signup</title>           
    </head>
   <body>
		<style>
			.error {{color: red;}}
		</style>
        <h1>Signup</h1>
        <form method="post">
            <table>
                <tbody>
                    <tr>
                        <td>
                            <label for="username">Username</label>
                        </td>
                        <td>
                            <input name="username" value="" type="text">
                            <span class="error">{username_error}</span>
                        </td>
                    </tr>
                     <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input name="password" value="" type="password">
                            <span class="error">{password_error}</span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input name="verify" value="" type="password">
                            <span class="error">{verify_error}</span>
                        </td>
                    </tr>
                     <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input name="email" value="">
                            <span class="error">{email_error}</span>
                        </td>
                    </tr>
                </tbody>
            </table>
            <input type="submit">
        </form>
    </body>
</html> 
"""

@app.route("/")
def index():
    return form.format(username="", username_error="", 
        password="", password_error="", verify="", 
        verify_error="", email="", email_error="")


@app.route("/", methods=['POST'])
def collect_user_input():
    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username = escape(username)
    password = escape(password)
    verify = escape(verify)
    email = escape(email)

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or " " in username or len(username) < 3 or len(username) > 20:
        username_error = "Invalid username"

    if password == "" or " " in password or len(password) < 3 or len(password) > 20:
        password_error = "Invalid password"

    if verify == "" or verify != password:
        verify_error = "Passwords do not match"
    
    else:
        return form.format(username=username, username_error=username_error, password=password, password_error=password_error, verify=verify, verify_error=verify_error)	

	
@app.route("/", methods=['POST'])
def form_values():
	resp = ""
	for field in request.form.keys():
		resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])
	return resp
	

app.run()