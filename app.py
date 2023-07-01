from flask import Flask, render_template

app = Flask(__name__, template_folder='assets')

users = {
    'user_1' : {
        'id' : 1,
        'username' : 'John',
        'age' : 10,
    },
    'user_2' : {
        'id' : 2,
        'username' : 'Kelly',
        'age' : 20,
    },
    'user_3' : {
        'id' : 3,
        'username' : 'Smith',
        'age' : 30,
    },
}

colors = ['red', 'green', 'blue']

@app.route("/home/")
def home_page():
    return render_template('index.html', students = users, colors = colors)


@app.route("/about/")
def about_page():
    return "<p>About Page</p>"