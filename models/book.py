from db import db

class BookModel(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.String(40), primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    subtitle = db.Column(db.String(80))
    authors = db.Relationship('Author', backref='book', lazy='dynamic')
    image_links = db.Relationship('Image', backref='book', lazy='dynamic')
    shelf = db.Column(db.String(40))

    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'title': self.title,
            'subtitle': self.subtitle,
            'authors': self.authors,
            'imageLinks': self.image_links,
            'shelf': self.shelf
        }

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)

    def __repr__(self):
        return '<Author %r>' % self.name
