from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, Length

class Update_Book(FlaskForm):
    title = StringField('New Title: ', validators=[DataRequired(), Length(min=2, max=100)])
    author = StringField('New Author: ', validators=[DataRequired(), Length(min=2, max=100)])
    pages = IntegerField('Pages: ', validators=[DataRequired()])
    cover = FileField('New Cover: ', validators=[FileAllowed(['jpg', 'png'])])
    
    submit = SubmitField('Update')
