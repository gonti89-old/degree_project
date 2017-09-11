from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SelectField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import datetime


class navigationForm(FlaskForm):
    instances = SelectField('instance',
                           validators=[DataRequired()],
                           default='instance_prod')
    dt = DateField('Date',
                   format='%Y-%m-%d',
                   default=datetime.date.today() - datetime.timedelta(days=1),
                   validators=[DataRequired()])

    periodType = SelectField('period',
                            validators=[DataRequired()],
                            default='period_day')

    country = SelectField('country',
                             validators=[DataRequired()])
