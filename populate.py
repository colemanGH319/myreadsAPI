from db import db
from models.book import BookModel

if __name__ == '__main__':
    db.create_all()
    book1 = BookModel("Le Petit Prince")
