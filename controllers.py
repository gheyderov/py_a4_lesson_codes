from app import app
from flask import render_template, request, redirect
from models import Product, Category, User, Contact
from forms import ContactForm, RegisterForm, LoginForm
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user

@app.route("/")
def home_page():
    products = Product.query.all()
    return render_template('index.html', product_lists = products)


@app.route("/login/", methods = ['GET', 'POST'])
def login_page():
    form = LoginForm()
    if request.method == 'POST':
        user = User.query.filter_by(username = form.username.data).first()
        # email = User.query.filter_by(email = form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            print('success')
            return redirect('/')
    return render_template('login.html', form = form)


@app.route("/register/", methods = ['GET', 'POST'])
def registration():
    form = RegisterForm()
    if request.method == 'POST':
        print('post')
        print(request.form)
        form = RegisterForm(request.form)
        if form.validate_on_submit():
            print('valid')
            user = User(
                username = form.username.data,
                email = form.email.data,
                password = generate_password_hash(form.password.data)
            )
            user.save()
    return render_template('register.html', form = form)


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
