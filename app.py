from flask import Flask
from flask_restful import Api
from resources.book import Book

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
api = Api(app)

api.add_resource(Books, '/books/<int:book_id>')

if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)
