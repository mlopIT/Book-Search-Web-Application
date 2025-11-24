"""
Flask-WTF form definitions for the Book Search application.
This module contains the search form with validation rules.
"""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length


class BookSearchForm(FlaskForm):
    """
    Form for searching books using the OpenLibrary API.
    
    Fields:
    - search_query: The search term (book title, author name, or subject)
    - search_type: Type of search (title, author, or subject)
    - result_limit: Maximum number of results to display (1-20)
    """
    
    search_query = StringField(
        'Search Query',
        validators=[
            DataRequired(message='Please enter a search term'),
            Length(min=1, max=200, message='Search query must be between 1 and 200 characters')
        ],
        render_kw={"placeholder": "e.g., Harry Potter, J.K. Rowling, Fantasy"}
    )
    
    search_type = SelectField(
        'Search By',
        choices=[
            ('title', 'Book Title'),
            ('author', 'Author Name'),
            ('subject', 'Subject/Topic')
        ],
        validators=[DataRequired()],
        default='title'
    )
    
    result_limit = IntegerField(
        'Number of Results',
        validators=[
            DataRequired(message='Please specify number of results'),
            NumberRange(min=1, max=20, message='Please choose between 1 and 20 results')
        ],
        default=10,
        render_kw={"placeholder": "1-20"}
    )
    
    submit = SubmitField('Search Books')
