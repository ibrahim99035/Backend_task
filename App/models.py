from App import db
from datetime import datetime

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    title = db.Column(db.String(100), nullable=False, default = 'none')
    num_of_page = db.Column(db.Integer, nullable=False, default = 0)
    author = db.Column(db.String(100), nullable=False, default = 'none')
    cover = db.Column(db.String(20), nullable=False, default = 'default.jpg')
    def __repr__(self):
        return f"The book: {self.title} for the Writer: {self.author}, has {self.num_of_page} pages, and has been added on {self.date_posted}"