from flask import Flask,  render_template, url_for, flash, redirect, request
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

@app.route("/find")
def dropdown_month():
    months =[{"name":"January"}, {"name":"February"}, {"name":"March"}, {"name":"April"}, {"name":"May"}, {"name":"June"}, {"name":"July"}, {"name":"August"}, {"name":"September"}, {"name":"October"}, {"name":"November"}, {"name":"December"}]
    return render_template("month1.html", months=months, title="Find")



@app.route("/check", methods=['GET', 'POST'])
def test():
    select = request.form.get('comp_select')
    if select == "January":
        with open("text_files/january.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "February":
         with open("text_files/february.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "March":
         with open("text_files/march.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "April":
         with open("text_files/april.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "May":
         with open("text_files/may.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "June":
         with open("text_files/june.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "July":
         with open("text_files/july.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "August":
         with open("text_files/august.txt", "r") as fopen:
            content = [row for row in fopen] 
    elif select == "September":
         with open("text_files/september.txt", "r") as fopen:
            content = [row for row in fopen] 
    elif select == "October":
         with open("text_files/october.txt", "r") as fopen:
            content = [row for row in fopen]  
    elif select == "November":
         with open("text_files/november.txt", "r") as fopen:
            content = [row for row in fopen]
    elif select == "December":
         with open("text_files/december.txt", "r") as fopen:
            content = [row for row in fopen]

    return render_template("text_jan.html", content=content)


if __name__ == "__main__":
    app.run(debug=True)