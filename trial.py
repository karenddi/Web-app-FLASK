from flask import Flask, render_template, url_for, flash, redirect, request
from forms import Registration_Form, Login_Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "9tjeq6ntl81f8zbj"



@app.route("/")
@app.route("/home")
def home():
    return render_template("home1.html")


@app.route("/about")
def about():
    return render_template("about1.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for("home"))
    return render_template("register1.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccesful! Please check username and password.", "danger")
    return render_template("login1.html", title="Login", form=form)

@app.route("/find", methods=["GET", "POST"])
def dropdown_month():
    months =["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    return render_template("month.html", months=months, title="Find")


if __name__ == "__main__":
    app.run(debug=True)