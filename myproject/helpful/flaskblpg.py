from flask import Flask, render_template, url_for, flash, redirect
from forms import Registration_Form, Login_Form

app = Flask(__name__)
app.config["SECRET_KEY"] = "9tjeq6ntl81f8zbj"
posts = [
    {
        "author" : "Karolina Dike",
        "title" : "Introduction",
        "content" : "First post",
        "date_posted" : "May 15, 2021"
    }, 

    {
        "author" : "Kamila Kowalska",
        "title" : "Blog post",
        "content" : "Second post",
        "date_posted" : "May 15, 2021"

        
    }


]


@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html", title="About")

@app.route("/register", methods=["GET", "POST"])
def register():
    form = Registration_Form()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Login_Form()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login unsuccesful! Please check username and password.", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)