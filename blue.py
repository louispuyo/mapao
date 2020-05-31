import django.utils.regex_helper as regex_helper
from flask.blueprints import Blueprint
from markupsafe import escape
import models
from flask import Flask, request

blue = Blueprint('blue', __name__)
db = Flask(__name__.split('.')[0])

@blue.route('/ok')
def okroute():
    return '{request:{pk}}'

@blue.route('/sd', methods=['GET', 'POST'])
def parsing():
    from models import mymodel

    model = request.args['model']
    model = mymodel
    return model().create()

@blue.endpoint('app.auth')
def authentification():
    return 'example'


@blue.app_template_filter('/<int:id>')
def search(db, id: int):
    return db[id]


