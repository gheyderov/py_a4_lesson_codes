from app import app
from flask import render_template, request
from models import Product, Category, User, Contact
from forms import ContactForm

@app.route("/")
def home_page():
    products = Product.query.all()
    return render_template('index.html', product_lists = products)


@app.route("/product/<int:id>/")
def product_detail(id):
    product = Product.query.filter_by(id = id).first()
    return render_template('product-detail.html', item = product)


@app.route("/contact/", methods = ['GET', 'POST'])
def contact_page():
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.form)
        print(request.form)
        if form.validate_on_submit():
            print('valid')
            contact = Contact(
                name = form.name.data,
                email = form.email.data,
                company = form.company.data,
                message = form.message.data,
                subscribe = form.subscribe.data
            )
            contact.save()
    return render_template('contact.html', form = form)
