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
    dt = tools.cast_to_date(session['data']['dt'])
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


@app.route('/', methods=['GET', 'POST'])
def instance_type():
    session['data'] = request.form.to_dict()

    form = initilize_forms_variables(request.form.to_dict())
    if form.validate_on_submit():
        country = session['data'].get('country')
        current_date = session['data'].get('dt')
        period_type = session['data'].get('periodType')
        instance_type = session['data'].get('instances')

        report_api = apiReports(country=country,
                                report_name='empty',
                                date=current_date,
                                period_type=period_type,
                                instance_type=instance_type
                                )

        reports_status = report_api.get_reports_statuses()
        plan_id = report_api.get_default_plan_id()
        return general_report_site(form, reports_status, plan_id)

    return render_template('base.html',
                           title='inital site',
                           form=form)


@app.route('/reports/<report_name>', methods=['POST', 'GET'])
def reports(report_name):

    form = read_session_form()
    country = request.args.get('country')
    current_date = request.args.get('dt')
    period_type = request.args.get('periodType')
    instance_type = request.args.get('instances')
    plan_id = int(request.args.get('plan_id'))

    report_api = apiReports(country=country,
                            report_name=report_name,
                            date=current_date,
                            period_type=period_type,
                            instance_type=instance_type,
                            plan_id=plan_id)

    reports_status = report_api.get_reports_statuses()
    plan_id = 1
    if form.validate_on_submit():
        return general_report_site(form, reports_status, plan_id)

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

    return render_template('basic_report.html',
                           name=report_name,
                           form=form,
                           plan_id=plan_id,
                           statuses=reports_status,
                           platforms=platforms,
                           url_params=request.args,
                           data=data
                           )