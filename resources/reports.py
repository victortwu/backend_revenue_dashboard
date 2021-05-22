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
        DATE='\ufeffDate'
        VENDOR='Doordash'
        WHOLESALE='True'
        SUBTOTAL='Subtotal'
        TAX='Tax'
        FEE='Fees'
        COMMISSION='Commission'
        TIP='Tip'
    #===== GRUBHUB =====
    if unique_key == 'Date':
        DATE='Date'
        VENDOR='Grubhub'
        WHOLESALE='True'
        SUBTOTAL='Subtotal'
        TAX='Tax'
        FEE='Processing Fee'
        COMMISSION='Commission'
        TIP='Tip'
    # #===== UBEREATS =====
    if unique_key == 'Dining Mode':
        DATE='Order Date / Refund date'
        VENDOR='UberEats'
        WHOLESALE='True'
        SUBTOTAL='Food Sales (excluding tax)'
        TAX='Tax on Food Sales'
        FEE='Order Processing Fee'
        COMMISSION='Uber Service Fee'
        TIP='Gratuity'
    # #===== KIOSKBUDDY =====
    if unique_key == 'Subtotal':
        DATE='Date'
        VENDOR='KioskBuddy'
        WHOLESALE='False'
        SUBTOTAL='Subtotal'
        TAX='Taxes'
        FEE='Promo Code' # This is a problem, Kioskbuddy has no fees or commision
        COMMISSION='Discount' # These 2 fields are ti fill in the gaps
        TIP='Tips'
    # #===== POSTMATES =====
    if unique_key == 'Order Number':
        DATE='Date'
        VENDOR='Postmates'
        WHOLESALE='False'
        SUBTOTAL='Subtotal'
        TAX='Tax'
        FEE='Fees'
        COMMISSION='Commission'
        TIP='' # same prob, no tips from PM, filled the gap



    # iterate here, had to hard code file name
    with open(file) as file:
        reader = csv.DictReader(file)

        for row in reader:
            uploaded_report = models.Report.create(
                date=row[DATE],
                vendor=VENDOR,
                wholesale=WHOLESALE,
                subtotal=row[SUBTOTAL],
                tax=row[TAX],
                fee=row[FEE],
                commission=row[COMMISSION],
                tip=row[TIP]
            )

            report_dict = model_to_dict(uploaded_report)

            print(report_dict)

    return jsonify(
        data = report_dict,
        message = 'Successfully uploaded report!',
        status = 201
    ), 201
