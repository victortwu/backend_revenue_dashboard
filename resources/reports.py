# =========== reports controller =============
import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

import csv

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
@reports.route('/<file>', methods=['POST'])
# pass in a parameter here that is the file?


def upload_report(file):



    # payload = request.get_json()
    #
    # print(payload)


    # iterate here, had to hard code file name
    with open(file) as file:
        reader = csv.DictReader(file)

        for row in reader:
            uploaded_report = models.Report.create(
                date=row['\ufeffDate'],
                vendor='Doordash',
                wholesale='True',
                subtotal=row['Subtotal'],
                tax=row['Tax'],
                fee=row['Fees'],
                commission=row['Commission'],
                tip=row['Tip']
            )

            report_dict = model_to_dict(uploaded_report)

            print(report_dict)

    return jsonify(
        data = report_dict,
        message = 'Successfully uploaded report!',
        status = 201
    ), 201
