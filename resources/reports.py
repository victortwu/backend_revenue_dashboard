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
    # control flow of which files so all type of files get same cutom fields
    first_read = csv.DictReader(open(file))
    unique_key = first_read.fieldnames[4]

    #===== DOORDASH =====
    if unique_key == 'Order':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:
                uploaded_report = models.Report.create(
                    date=row['\ufeffDate'],
                    vendor='Doordash',
                    wholesale='true',
                    subtotal=float(row['Subtotal'].replace('$', '')),
                    tax=float(row['Tax'].replace('$', '')),
                    fee=row['Fees'],
                    commission=float(row['Commission'].replace('($', '-').replace(')', '')),
                    tip=float(row['Tip'].replace('$', ''))
                )

                report_dict = model_to_dict(uploaded_report)

                print(report_dict)

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
                uploaded_report = models.Report.create(
                    date=row['Date'],
                    vendor='Grubhub',
                    wholesale='true',
                    subtotal=row['Subtotal'],
                    tax=row['Tax'],
                    fee=row['Processing Fee'],
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


    # #===== UBEREATS =====
    if unique_key == 'Dining Mode':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:
                uploaded_report = models.Report.create(
                    date=row['Order Date / Refund date'],
                    vendor='UberEats',
                    wholesale='true',
                    subtotal=row['Food Sales (excluding tax)'],
                    tax=row['Tax on Food Sales'],
                    fee=row['Order Processing Fee'],
                    commission=row['Uber Service Fee'],
                    tip=row['Gratuity']
                )

                report_dict = model_to_dict(uploaded_report)

                print(report_dict)

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
                uploaded_report = models.Report.create(
                    date=row['Date'],
                    vendor='KioskBuddy',
                    wholesale='false',
                    subtotal=float(row['Subtotal']),
                    tax=float(row['Taxes']),
                    fee=0,
                    commission=0,
                    tip=float(row['Tips'])
                )

                report_dict = model_to_dict(uploaded_report)

                print(report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201

    # #===== POSTMATES =====
    if unique_key == 'Order Number':
        with open(file) as file:
            reader = csv.DictReader(file)

            for row in reader:
                uploaded_report = models.Report.create(
                    date=row['Date'],
                    vendor='Postmates',
                    wholesale='false',
                    subtotal=row['Subtotal'],
                    tax=row['Tax'],
                    fee=row['Fees'],
                    commission=row['Commission'],
                    tip=0
                )

                report_dict = model_to_dict(uploaded_report)

                print(report_dict)

        return jsonify(
            data = report_dict,
            message = 'Successfully uploaded report!',
            status = 201
        ), 201
