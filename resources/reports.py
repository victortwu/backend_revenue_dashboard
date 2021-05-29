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
@reports.route('/<file>', methods=['GET', 'POST']) #right now files are in folder on machine
# pass in a parameter here that is the file?
# where to put files first before putting in DB??

def upload_report(file):
    # control flow of which files so all type of files get same cutom fields
    first_read = csv.DictReader(open(file))
    unique_key = first_read.fieldnames[4]

    #===== POSTMATES =====
    if unique_key == 'Order':
        with open(file) as file:
            reader = csv.DictReader(file)
                # start loop here
            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['\ufeffDate']))
                    print('Try ======== ', report_dict)

                except models.DoesNotExist:

                    uploaded_report = models.Report.create(
                        date=row['\ufeffDate'],
                        vendor='Postmates',
                        wholesale='false',
                        subtotal=float(row['Subtotal'].replace('$', '')),
                        tax=float(row['Tax'].replace('$', '')),
                        fee=row['Fees'],
                        commission=float(row['Commission'].replace('($', '-').replace(')', '')),
                        tip=float(row['Tip'].replace('$', '')),
                        unique_id=row['\ufeffDate']
                    )

                    report_dict = model_to_dict(uploaded_report)

                    print('Except ====== ', report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201


    #===== GRUBHUB =====
    if unique_key == 'Date':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['ID']))
                    print('Try:.....', report_dict)

                except models.DoesNotExist:

                    uploaded_report = models.Report.create(
                        date=row['Date'],
                        vendor='Grubhub',
                        wholesale='true',
                        subtotal=row['Subtotal'],
                        tax=row['Tax'],
                        fee=row['Processing Fee'],
                        commission=row['Commission'],
                        tip=row['Tip'],
                        unique_id=row['ID']
                    )

                    report_dict = model_to_dict(uploaded_report)

                    print('EXCEPT======= ', report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201


    # #===== UBEREATS =====
    if unique_key == 'Dining Mode':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['Order ID']))
                    print('Try:.....', report_dict)

                except models.DoesNotExist:


                    uploaded_report = models.Report.create(
                        date=row['Order Date / Refund date'],
                        vendor='UberEats',
                        wholesale='true',
                        subtotal=row['Food Sales (excluding tax)'],
                        tax=row['Tax on Food Sales'],
                        fee=row['Order Processing Fee'],
                        commission=row['Uber Service Fee'],
                        tip=row['Gratuity'],
                        unique_id=row['Order ID']
                    )

                    report_dict = model_to_dict(uploaded_report)

                    print('EXCEPT======= ', report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201


    # #===== KIOSKBUDDY =====
    if unique_key == 'Subtotal':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['Transaction Client ID']))
                    print('Try=======', report_dict)

                except models.DoesNotExist:

                    uploaded_report = models.Report.create(
                        date=row['Date'],
                        vendor='KioskBuddy',
                        wholesale='false',
                        subtotal=float(row['Subtotal']),
                        tax=float(row['Taxes']),
                        fee=0,
                        commission=0,
                        tip=float(row['Tips']),
                        unique_id=row['Transaction Client ID']
                    )

                    report_dict = model_to_dict(uploaded_report)

                    print(report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201

    # #===== DOORDASH =====
    if unique_key == 'PAYOUT_TIME':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['TRANSACTION_ID']))
                    print('Try:.....', report_dict)

                except models.DoesNotExist:
                    if row['TRANSACTION_TYPE'] != 'PAYOUT':
                        uploaded_report = models.Report.create(
                            date=row['TIMESTAMP_LOCAL_DATE'],
                            vendor='Doordash',
                            wholesale='true',
                            subtotal=row['SUBTOTAL'],
                            tax=row['TAX_REMITTED_BY_DOORDASH_TO_STATE'],
                            fee=float(row['MARKETING_FEES']) * -1,
                            commission=float(row['COMMISSION']) * -1,
                            tip=row['STAFF_TIP'],
                            unique_id=row['TRANSACTION_ID']
                        )

                        report_dict = model_to_dict(uploaded_report)

                        print('Except ======  ', report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201
