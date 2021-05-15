from flask import Flask, render_template, url_for
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

@app.route("/register")
def register():
    form = Registration_Form()
    return render_template("register.html", title="Register", form=form)

@app.route("/login")
def login():
    form = Login_Form()
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    app.run(debug=True)