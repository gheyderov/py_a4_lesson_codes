from flask import Flask, render_template

app = Flask(__name__)

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

products = {
    1 : {
        'id' : 1,
        'title' : 'Product #1',
        'price' : 100,
        'description' : 'Some Description #1',
        'image': 'p1.avif',
        'colors': ['blue', 'red'],
    },
    2 : {
        'id' : 2,
        'title' : 'Product #2',
        'price' : 200,
        'description' : 'Some Description #2',
        'image': 'p2.avif',
        'colors': ['black', 'red']
    },
    3 : {
        'id' : 3,
        'title' : 'Product #3',
        'price' : 300,
        'description' : 'Some Description #3',
        'image': 'p3.avif',
        'colors': ['green', 'white']
    }

}

@app.route("/")
def home_page():
    return render_template('index.html', product_lists = products)


@app.route("/product/<int:id>/")
def product_detail(id):
    product = products[id]
    return render_template('product-detail.html', item = product)

