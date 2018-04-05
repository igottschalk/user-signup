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
                            <span class="error"></span>
                        </td>
                    </tr>
                     <tr>
                        <td>
                            <label for="password">Password</label>
                        </td>
                        <td>
                            <input name="password" value="" type="password">
                            <span class="error"></span>
                        </td>
                    </tr>
                    <tr>
                        <td>
                            <label for="verify">Verify Password</label>
                        </td>
                        <td>
                            <input name="verify" value="" type="password">
                            <span class="error"></span>
                        </td>
                    </tr>
                     <tr>
                        <td>
                            <label for="email">Email (optional)</label>
                        </td>
                        <td>
                            <input name="email" value="">
                            <span class="error"></span>
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
    return form
	
@app.route("/", methods=['POST'])
def form_values():
	resp = ""
	for field in request.form.keys():
		resp += "<b>{key}</b>: {value}<br>".format(key=field, value=request.form[field])
	return resp
	

app.run()