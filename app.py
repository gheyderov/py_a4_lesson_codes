from flask import Flask, render_template

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345@127.0.0.1:3306/project'
app.config['SECRET_KEY'] = 'project'

from controllers import *
from models import *
from extensions import *


if '__name__' == '__main__':
    app.init_app(db)
    app.init_app(migrate)