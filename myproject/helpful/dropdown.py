from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = True


@app.route('/', methods=['GET'])

def dropdown_month():
    months =["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
    return render_template('month.html', months=months)

@app.route('/select', methods=['GET'])

def dropdown_veggies_or_fruit():
    plants =["veggies", "fruit", "veggies and fruit"]
    return render_template('test1.html', plants=plants)


if __name__ == "__main__":
    app.run()


