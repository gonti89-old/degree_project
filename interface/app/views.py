import forms
import tools
from app import app
from flask import flash
from flask import session
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from read_data_from_db import apiReports

def update_session():
    session['data'] = request.form.to_dict()


def general_report_site(form, statuses, plan_id):
    update_session()
    return render_template('general_reports_site.html',
                           title='test',
                           form=form,
                           statuses=statuses,
                           plan_id=plan_id)

def read_session_form():
    dt=tools.cast_to_date(session['data']['dt'])
    form = forms.navigationForm(instances=session['data']['instances'],
                                country=session['data']['country'],
                                periodType=session['data']['periodType'],
                                dt=dt)
    return form



def initilize_forms_variables(data):
    form = forms.navigationForm()

    form.instances.choices = tools.get_instances()
    form.periodType.choices = tools.get_period_types()
    form.country.choices = tools.get_countries()
    return form

@app.route('/', methods = ['GET', 'POST'])
def instance_type():
    session['data'] = request.form.to_dict()

    form = initilize_forms_variables(request.form.to_dict())
    reports_status = tools.get_reports_statuses()
    plan_id = 1
    if form.validate_on_submit():
        return render_template('general_reports_site.html',
                               title='test',
                               form=form,
                               statuses=reports_status,
                               plan_id=plan_id)

    return render_template('base.html',
                           title='inital site',
                           form=form)

@app.route('/error', methods=['POST', 'GET'])
def error_site():
    form = read_session_form()
    reports_status = tools.get_reports_statuses()
    plan_id = 1
    if form.validate_on_submit():
        return render_template('general_reports_site.html',
                                title='test',
                                form=form,
                                statuses=reports_status,
                                plan_id=plan_id)

    return render_template('error_site.html',
                           title='error',
                           form=form,
                           statuses=reports_status,
                           plan_id=plan_id
                           )


@app.route('/second_report', methods=['POST', 'GET'])
def second_report():

    form = read_session_form()

    reports_status = tools.get_reports_statuses()
    plan_id = 1
    if form.validate_on_submit():
       return general_report_site(form, reports_status, plan_id)

    country = request.args.get('country')
    current_date = request.args.get('dt')
    period_type = request.args.get('periodType')
    instance_type= request.args.get('instances')
    plan_id = int(request.args.get('plan_id'))
    report_api = apiReports(country=country,
                            report_name="basicStatsTrend",
                            date=current_date,
                            period_type=period_type,
                            instance_type=instance_type,
                            plan_id=plan_id)
    try:
        data = report_api.create_report()

    except ValueError as e:

        return render_template('error_site.html',
                               title='error',
                               form=form,
                               statuses=reports_status,
                               url_params=request.args,
                               error_message=e,
                               plan_id=plan_id
                               )
    platforms = report_api.find_plans_id('on')

    chartID = data['title']['text']
    series = data['series']
    chart_title = data['title']
    chart = data['chart']
    xAxis = data['xAxis']
    yAxis = {'title': {'text': 'testlabel'}}

    return render_template('first_report.html',
                           form=form,
                           statuses=reports_status,
                           platforms=platforms,
                           url_params=request.args,
                           chartID=chartID,
                           series=series,
                           chart_title=chart_title,
                           chart=chart,
                           xAxis=xAxis,
                           yAxis=yAxis
                           )


@app.route('/first_report', methods=['POST', 'GET'])
def first_report():
    form = initilize_forms_variables()
    reports_status = tools.get_reports_statuses()
    platforms = tools.get_platforms()

    chartID = 'chart_ID'
    chart_type = 'bar'
    chart_height = 350
    #
    chart = {"type": chart_type, "height": chart_height}
    series = [{"name": 'Label1', "data": [1, 2, 3]}, {"name": 'Label2', "data": [4, 5, 6]}]
    chart_title = {"text": 'My Title'}
    xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    yAxis = {"title": {"text": 'yAxis Label'}}

    if form.validate_on_submit():
        for filled_field in form:
            if filled_field.short_name != 'csrf_token':
                flash("chosen '%s' : '%s'" % (filled_field.label.text, filled_field.data))
        return redirect(url_for('reports',
                                instance=form.instances.data,
                                country=form.country.data,
                                period=form.periodType.data,
                                report_date=form.dt.data,
                                form=form))

    return render_template('first_report.html',
                           form=form,
                           statuses=reports_status,
                           platforms=platforms,
                           url_params=request.args,
                           chartID=chartID,
                           series=series,
                           chart_title=chart_title,
                           chart=chart,
                           xAxis=xAxis,
                           yAxis=yAxis
                           )
