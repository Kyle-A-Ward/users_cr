from flask import Flask, render_template, redirect, request
from user import User
app = Flask(__name__)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("create.html", all_users=users)
@app.route("/create_user", methods=["POST"])
def render_lists():
    data = {
        "firstname": request.form["firstname"],
        "lastname": request.form["lastname"],
        "email": request.form["email"]
    }
    User.save(data)
    return redirect("/read")
@app.route("/read")
def read():
    users = User.get_all()
    return render_template("read.html", all_users=users)
if __name__ == "__main__":
    app.run(debug=True)