
# users = {
#     'user_1' : {
#         'id' : 1,
#         'username' : 'John',
#         'age' : 10,
#     },
#     'user_2' : {
#         'id' : 2,
#         'username' : 'Kelly',
#         'age' : 20,
#     },
#     'user_3' : {
#         'id' : 3,
#         'username' : 'Smith',
#         'age' : 30,
#     },
# }

# colors = ['red', 'green', 'blue']

# products = {
#     1 : {
#         'id' : 1,
#         'title' : 'Product #1',
#         'price' : 100,
#         'description' : 'Some Description #1',
#         'image': 'p1.avif',
#         'colors': ['blue', 'red'],
#     },
#     2 : {
#         'id' : 2,
#         'title' : 'Product #2',
#         'price' : 200,
#         'description' : 'Some Description #2',
#         'image': 'p2.avif',
#         'colors': ['black', 'red']
#     },
#     3 : {
#         'id' : 3,
#         'title' : 'Product #3',
#         'price' : 300,
#         'description' : 'Some Description #3',
#         'image': 'p3.avif',
#         'colors': ['green', 'white']
#     }

# }

from extensions import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(100), nullable = False)
    age = db.Column(db.Integer)

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def __repr__(self):
        return self.username
    
    def save(self):
        db.session.add(self)
        db.session.commit()


product_color = db.Table('product_color',
                    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
                    db.Column('color_id', db.Integer, db.ForeignKey('color.id'))
                    )

product_size = db.Table('product_size',
                    db.Column('product_id', db.Integer, db.ForeignKey('product.id')),
                    db.Column('size_id', db.Integer, db.ForeignKey('size.id'))
                    )

class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(155))
    price = db.Column(db.Integer)
    description = db.Column(db.String(255), nullable = True)
    image = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    colors = db.relationship('Color', secondary=product_color, backref='products')
    sizes = db.relationship('Size', secondary=product_size, backref='products')
    images = db.relationship('ProductImage', backref = 'product')

    def __init__(self, title, price, description, image, category_id):
        self.title = title
        self.price = price
        self.description = description
        self.image = image
        self.category_id = category_id

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class ProductImage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    image = db.Column(db.String(155))
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'))

    def __init__(self, image, product_id):
        self.image = image
        self.product_id = product_id

    def __repr__(self):
        return self.image
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Color(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Size(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100))

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(155))
    products = db.relationship(Product, backref = 'category')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return self.title
    
    def save(self):
        db.session.add(self)
        db.session.commit()


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    company = db.Column(db.String(100))
    message = db.Column(db.Text)
    subscribe = db.Column(db.Boolean)

    def __init__(self, name, email, company, message, subscribe):
        self.name = name
        self.email = email
        self.company = company
        self.message = message
        self.subscribe = subscribe

    def __repr__(self):
        return self.name
    
    def save(self):
        db.session.add(self)
        db.session.commit()