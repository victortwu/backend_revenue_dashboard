# =========== reports controller =============
import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

#========================================

reports = Blueprint('reports', 'reports')

#========= ROUTES =============


#----GET REPORTS----
@reports.route('/', methods=['GET'])

def reports_index():

    report_dicts = [model_to_dict(report) for report in models.Report.select()]

    print(report_dicts)

    return jsonify({
        'data': report_dicts,
        'message': f'Successfully found {len(report_dicts)} reports.',
        'status': 200
    }), 200


#----CREATE (upload) REPORTS-----
@reports.route('/', methods=['POST'])

def upload_report():

    payload = request.get_json()

    print(payload)

    uploaded_report = models.Report.create(
        date=payload['date'],
        vendor=payload['vendor'],
        wholesale=payload['wholesale'],
        subtotal=payload['subtotal'],
        tax=payload['tax'],
        fee=payload['fee'],
        commission=payload['commission']
    )

    report_dict = model_to_dict(uploaded_report)

    return jsonify(
        data = report_dict,
        message = 'Successfully uploaded report!',
        status = 201
    ), 201
