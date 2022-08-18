from flask_wtf import FlaskForm
from wtforms import SubmitField, SearchField
from wtforms.validators import DataRequired

class PatientSearch(FlaskForm):
    search  = SearchField('Search a book', validators=[DataRequired()])
    submit = SubmitField('Search')