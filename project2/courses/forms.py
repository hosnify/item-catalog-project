
from flask_wtf import FlaskForm
from wtforms.fields import StringField  , SubmitField  , TextAreaField ,IntegerField
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField 
from project2.models import Category


class courseForm(FlaskForm):
    name= StringField('Course name' , validators = [DataRequired()] )
    price = IntegerField('Course price' , validators = [DataRequired()] )
    description=TextAreaField('Course description', validators = [DataRequired()])
    Category = QuerySelectField(
        'Category',
        query_factory=lambda: Category.query ,
        get_label='name' ,
        allow_blank=False
    )
    submit= SubmitField('submit' )
