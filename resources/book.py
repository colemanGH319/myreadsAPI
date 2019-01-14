from flask_restful import Resource
from models.book import BookModel

class Book(Resource):
    def get(self, name):
        book = BookModel.find_by_name(name)
        if book:
            return book.json()
        return {'message': 'Book not found'}, 404

    
