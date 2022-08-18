from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length, ValidationError

from App.models import Book

class Add_Book(FlaskForm):
    title = StringField('Book Title: ', validators=[DataRequired(), Length(min=2, max=100)])
    author = StringField('Author of the book: ', validators=[DataRequired(), Length(min=2, max=100)])
    pages = IntegerField('Number of pages: ', validators=[DataRequired()])
    cover = FileField('Cover of the book: ', validators=[FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Add Book')

    def validate_title(self, title):
        book = Book.query.filter_by(title=title.data).first()
        if book:
            raise ValidationError('That book is already in the database. Please choose a different title.')