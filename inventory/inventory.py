from flask import Blueprint
from .extensions import mongo

main = Blueprint('main', __name__)


@main.route('/')
def index():
    book_collection = mongo.db.books
    book_collection.insert(
                            {
                                'tittle': 'Uma Breve História do Tempo',
                                'author': 'Stephen Hawking',
                                'year': 2015,
                                'pages': 255
                            }
                        )
    return '<h1>Added a Book!</h1>'
