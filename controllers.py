from app import app
from flask import render_template
from models import Product, Category, User

@app.route("/")
def home_page():
    products = Product.query.all()
    return render_template('index.html', product_lists = products)


@app.route("/product/<int:id>/")
def product_detail(id):
    product = Product.query.filter_by(id = id).first()
    return render_template('product-detail.html', item = product)

