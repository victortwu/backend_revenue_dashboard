# =========== reports controller =============
import models

from flask import Blueprint, request, jsonify

from playhouse.shortcuts import model_to_dict

from flask_login import current_user, login_required

from datetime import datetime

import csv



#========================================

reports = Blueprint('reports', 'reports')

#========= ROUTES =============


#----GET REPORTS----
@reports.route('/<dates>', methods=['GET'])
# this route needs to pass in date params
def reports_index(dates):# date params pass in function

    date_range = dates.split(',')
    st_date_str = date_range[0]
    e_date_str = date_range[1]
    slice_object = slice(15)
    sliced_start = date_range[0][slice_object]
    sliced_end = date_range[1][slice_object]
    start_date = datetime.strptime(sliced_start, '%a %b %d %Y').strftime('%Y-%m-%d')
    end_date = datetime.strptime(sliced_end, '%a %b %d %Y').strftime('%Y-%m-%d')

    report_dicts = [model_to_dict(report) for report in models.Report.select().where(models.Report.date.between(start_date, end_date))]

    print(report_dicts)

    return jsonify({
        'data': report_dicts,
        'message': f'Successfully found {len(report_dicts)} reports.',
        'status': 200
    }), 200


#----CREATE (upload) REPORTS-----
@reports.route('/', methods=['POST'])
# pass in a parameter here that is the file?


def upload_report():
    # control flow of which files so all type of files get same custom fields
    payload = request.get_data()

    str_data = payload.decode('utf-8')
    print(str_data)
    # first_read = csv.DictReader(str_data.splitlines())
    # unique_key = first_read.fieldnames[4]
    # print(unique_key)
    reader = csv.DictReader(str_data.splitlines())
            # start loop here
    for row in reader:
        uploaded_report = models.Report.create(
            date=row['Order Date / Refund date'],
            vendor='UberEats',
            wholesale='true',
            subtotal=row['Food Sales (excluding tax)'],
            tax=row['Tax on Food Sales'],
            fee=row['Order Processing Fee'],
            commission=row['Uber Service Fee'],
            tip=row['Gratuity'],
            unique_id=float(row['Order ID'])
        )

    report_dict = model_to_dict(uploaded_report)
    print(report_dict)

    return payload
    try:
        payload = request.get_data()

        str_data = payload.decode('utf-8')

        first_read = csv.DictReader(str_data.splitlines())
        unique_key = first_read.fieldnames[4]
        print(unique_key)









        #===== POSTMATES =====
        if unique_key == 'Order':
            # with open(file) as file:
            reader = csv.DictReader(str_data.splitlines())
                    # start loop here
            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['Date']))
                    print('Try ======== ', report_dict)

                except models.DoesNotExist:
                    for row in reader:
                        slice_object = slice(15)
                        sliced_date = row['Date'][slice_object]
                        uploaded_report = models.Report.create(
                            date=datetime.strptime(sliced_date, '%a %b %d %Y').strftime('%Y-%m-%d'),
                            vendor='Postmates',
                            wholesale='false',
                            subtotal=float(row['Subtotal'].replace('$', '')),
                            tax=float(row['Tax'].replace('$', '')),
                            fee=float(row['Fees'].replace('$', '')),
                            commission=float(row['Commission'].replace('($', '-').replace(')', '')),
                            tip=float(row['Tip'].replace('$', '')),
                            unique_id=float(row['Order'])
                        )
                    # slice_object = slice(15)
                    # sliced_date = row['Date'][slice_object]
                    # uploaded_report = models.Report.create(
                    #     date=datetime.strptime(sliced_date, '%a %b %d %Y').strftime('%Y-%m-%d'),
                    #     vendor='Postmates',
                    #     wholesale='false',
                    #     subtotal=float(row['Subtotal'].replace('$', '')),
                    #     tax=float(row['Tax'].replace('$', '')),
                    #     fee=row['Fees'],
                    #     commission=float(row['Commission'].replace('($', '-').replace(')', '')),
                    #     tip=float(row['Tip'].replace('$', '')),
                    #     unique_id=row['Date']
                    # )

                    report_dict = model_to_dict(uploaded_report)

                    print('Except ====== ', report_dict)

            return jsonify(
                data = report_dict,
                message = 'Successfully uploaded report!',
                status = 201
            ), 201


        #===== GRUBHUB =====
        if unique_key == 'Date':

            reader = csv.DictReader(str_data.splitlines())

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['ID']))
                    print('Try:.....', report_dict)

                except models.DoesNotExist:
                    uploaded_report = models.Report.create(
                        date=datetime.strptime(row['Date'], '%x').strftime('%Y-%m-%d'),
                        vendor='Grubhub',
                        wholesale='true',
                        subtotal=row['Subtotal'],
                        tax=row['Tax'],
                        fee=row['Processing Fee'],
                        commission=row['Commission'],
                        tip=row['Tip'],
                        unique_id=float(row['ID'].replace('O-', ''))
                    )


                    # uploaded_report = models.Report.create(
                    #     date=datetime.strptime(row['Date'], '%x').strftime('%Y-%m-%d'),
                    #     vendor='Grubhub',
                    #     wholesale='true',
                    #     subtotal=row['Subtotal'],
                    #     tax=row['Tax'],
                    #     fee=row['Processing Fee'],
                    #     commission=row['Commission'],
                    #     tip=row['Tip'],
                    #     unique_id=row['ID']
                    # )

                    report_dict = model_to_dict(uploaded_report)

                    print('EXCEPT======= ', report_dict)

            return jsonify(
                data = report_dict,
                message = 'Successfully uploaded report!',
                status = 201
            ), 201


        # #===== UBEREATS =====
        if unique_key == 'Dining Mode':

            reader = csv.DictReader(str_data.splitlines())

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

            reader = csv.DictReader(str_data.splitlines())

            for row in reader:

                try:
                    report_dict = model_to_dict(models.Report.get(models.Report.unique_id == row['Transaction Client ID']))
                    print('Try=======', report_dict)

                except models.DoesNotExist:
                    slice_object = slice(10)
                    sliced_date = row['Date'][slice_object]
                    uploaded_report = models.Report.create(
                        date=datetime.strptime(sliced_date, '%m/%d/%Y').strftime('%Y-%m-%d'),
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

            reader = csv.DictReader(str_data.splitlines())

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

    except:

        return jsonify(
            data = {},
            message = 'This file can not be accepted! Click on COMPLIANT FILES ONLY for more info.',
            status = 500
        ), 500
