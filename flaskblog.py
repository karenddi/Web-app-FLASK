from flask import Flask, render_template, url_for

app = Flask(__name__)
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

if __name__ == "__main__":
    app.run(debug=True)