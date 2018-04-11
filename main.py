from flask import Flask, request, redirect, render_template
import cgi


app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/")
def index():
    return render_template('signup.html')


@app.route("/", methods=['POST'])
def collect_user_input():

    username = request.form['username']
    password = request.form['password']
    verify = request.form['verify']
    email = request.form['email']

    username_error = ""
    password_error = ""
    verify_error = ""
    email_error = ""

    if username == "" or " " in username:
        username_error = "Invalid username"

    if len(username) < 3 or len(username) > 20:
        username_error = "Invalid username"

    if len(password) < 3 or len(password) > 20:
        password_error = "Invalid password"

    if verify != password:
        verify_error = "Passwords do not match"

    if email != "":
        if "@" not in email or "." not in email or " " in email or len(email) < 3 or len(email) > 20:
            email_error = "Invalid email" 

    if len(username_error) > 0 or len(password_error) > 0 or len(verify_error) > 0:
        return render_template('signup.html', username=username, username_error=username_error, 
            password=password, password_error=password_error, verify=verify, verify_error=verify_error, email=email, email_error=email_error)
    else:
        return render_template('welcome.html', username=username)  
        
	
@app.route("/Welcome", methods=['POST'])
def form_values():
	resp = ""
	for field in request.form.keys():
		resp += "{key}: {value}".format(key=field, value=request.form[field])
	return "Welcome"
	
app.run()