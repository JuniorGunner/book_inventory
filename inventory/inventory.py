from flask import Blueprint, Flask
from .extensions import mongo

# main = Blueprint('main', __name__)
app = Flask(__name__)


@app.route('/')
def index():
    book_collection = mongo.db.books
    book_collection.insert(
                            {
                                'title': 'Uma Breve História do Tempo',
                                'author': 'Stephen Hawking',
                                'year': 2015,
                                'pages': 255
                            }
                        )
    return '<h1>Added a Book!</h1>'


app.run(debug=True)
