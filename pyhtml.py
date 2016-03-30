from flask import Flask, request, render_template
from user import load_users, save_users

app = Flask(__name__)


@app.route("/")
def users():
	brukere = ["Jonas", "Glenn", "Robin"]
	return render_template("users.html", users=brukere)


@app.route("/<username>")
def profile(username):
	users = load_users()
	user = users[username]
	return render_template("profile.html", user=user)



if __name__ == '__main__':
	import webbrowser
	webbrowser.open("http://localhost:5000")
	app.run(debug=True)
