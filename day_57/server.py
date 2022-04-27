from flask import Flask, render_template
import random
import datetime
import requests

# export FLASK_ENV=development
"""we all know that the python run python scripts and now how can we put our blog(html file) and our python script together
 ? this is the case where jinja come in very handy. jinja will sort interpreted to python what is html and what is a it 
 script"""
# we can render html template using the flask class render_template

app = Flask(__name__)


# first we need a flask simple application
# how to use  python datetime module to print only the current date and time
# now = datetime.datetime.now().year

#
@app.route("/home/<name>")
def home(name):
    now = datetime.datetime.now()
    right = now.strftime("%Y")
    num = random.randint(1, 10)
    return render_template("index.html", john_age=num, copy_right=right, guess_name=name)


# use the request module


@app.route("/guess/<name>/<numb>")
def guess(name, numb):
    age_answer = requests.get(f"https://api.agify.io?name={name}")
    age_answer.raise_for_status()
    age_data = age_answer.json()
    age = age_data["age"]

    answer = requests.get(f"https://api.genderize.io?name={name}")
    answer.raise_for_status()
    gender_data = answer.json()
    gender = gender_data["gender"]
    return render_template("my_guess.html", guess_name=name, guess_gender=gender, guess_age=age, numE=numb)


# HOW TO USE FOR LOOP AND IF STATEMENT INSIDE THE HTML FILE USING JINJA


@app.route("/blog/mama")
def blog():
    """the api is not working for this example"""
    url = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(url)
    response.raise_for_status()
    post_data = response.json()
    return render_template("my_blog.html", posts=post_data)

# JINJA CAN ALSO HELP US TO ASSESS DIFFERENT URL
# IN THE DOCUMENTATION WE CAN FIND IT UNDER URL FOR METHODS
if __name__ == "__main__":
    app.run(debug=True)
