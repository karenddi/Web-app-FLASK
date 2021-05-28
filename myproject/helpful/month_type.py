from flask import Flask, render_template, request, jsonify
#from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import SelectField

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
#app.config["SQLALCHEMY_TRACK_MODIFICATIONS "]=False
app.config["SECRET_KEY"] = "9tjeq6ntl81f8zbj"

#db = SQLAlchemy(app)


# class Month_Selection(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     month = db.Column(db.String())

# class Veggies_Fruit(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     your_selection = db.Column(db.String())

class Form(FlaskForm):
    month = SelectField("month", choices=[("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")])
    your_selection = SelectField("your_selection", choices=["veggies", "fruit"])


@app.route("/")
@app.route("/select", methods=["GET", "POST"])

def selection():
    form = Form()
    return render_template("index.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)

