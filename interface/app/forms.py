from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SelectField, Form
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
import datetime
import tools


class navigationForm(FlaskForm):
    instances = SelectField('instance',
                            validators=[DataRequired()],
                            default='prod',
                            choices=tools.get_instances())
    dt = DateField('Date',
                   format='%Y-%m-%d',
                   default=datetime.date.today() - datetime.timedelta(days=1),
                   validators=[DataRequired()])

    periodType = SelectField('period',
                             validators=[DataRequired()],
                             default='period_day',
                             choices=tools.get_period_types())

    country = SelectField('country',
                          validators=[DataRequired()],
                          choices=tools.get_countries())
