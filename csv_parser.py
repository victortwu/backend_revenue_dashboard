import csv
from datetime import datetime
# reader = csv.DictReader(open('ubereats_sample.csv'))
# print('UberEats key: ', reader.fieldnames[4])
#
# reader = csv.DictReader(open('Deliveries.csv'))
# print('Doordash key: ', reader.fieldnames[4])
#
# reader = csv.DictReader(open('grubhub_sample.csv'))
# print('Grubhub key: ', reader.fieldnames[4])
#
# reader = csv.DictReader(open('kb_sample.csv'))
# print('KioskBuddy key: ', reader.fieldnames[4])
#
# reader = csv.DictReader(open('postmates_sample.csv'))
# print('Postmates key: ', reader.fieldnames[4])

date_range_str = 'Thu Apr 01 2021 00:00:00 GMT-0700 (Pacific Daylight Time),Wed Apr 14 2021 00:00:00 GMT-0700 (Pacific Daylight Time)'
# %a %b %d %Y %X %Z

# split_dates = date_range.replace(",", '","')
#
# make_list = [split_dates]
# print(len(make_list))
# print(type(make_list))
date_range_list = date_range_str.split(',')
print(len(date_range_list))
print(type(date_range_list))
print(date_range_list)
print(type(date_range_list[0]))
print(date_range_list[1])


slice_object = slice(15)
sliced_date = date_range_list[0][slice_object]



formatted = datetime.strptime(sliced_date, '%a %b %d %Y').strftime('%Y-%m-%d')
print('Here is formatted: ', formatted)

# ======== a doordash file ===========
# with open('doordash_sample.csv') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print('===========================')
        # print('')
        # print('TIMESTAMP_UTC_TIME  ', row['TIMESTAMP_UTC_TIME'])
        # print('TIMESTAMP_UTC_DATE  ', row['TIMESTAMP_UTC_DATE'])
        # print('TIMESTAMP_LOCAL_TIME  ', row['TIMESTAMP_LOCAL_TIME'])
        # print('TIMESTAMP_LOCAL_DATE   ', row['TIMESTAMP_LOCAL_DATE'])
        # print('')
        # print('PAYOUT_TIME   ', row['PAYOUT_TIME'])
        # print('BUSINESS_ID   ', row['BUSINESS_ID'])
        # print('STORE_NAME   ', row['STORE_NAME'])
        # print('MERCHANT_STORE_ID   ', row['MERCHANT_STORE_ID'])
        # print('')
        # print('TRANSACTION_TYPE   ', row['TRANSACTION_TYPE'])
        # # print('TRANSACTION_ID   ', row['TRANSACTION_ID'])
        # # print('DOORDASH_ORDER_ID   ', row['DOORDASH_ORDER_ID'])
        # # print('MERCHANT_DELIVERY_ID   ', row['MERCHANT_DELIVERY_ID'])
        # # print('')
        # # print('EXTERNAL_ID   ', row['EXTERNAL_ID'])
        # # print('DESCRIPTION   ', row['DESCRIPTION'])
        # # print('FINAL_ORDER_STATUS   ', row['FINAL_ORDER_STATUS'])
        # # print('CURRENCY   ', row['CURRENCY'])
        # print('')
        # print('SUBTOTAL   ', row['SUBTOTAL'])
        # # print('TAX_SUBTOTAL   ', row['TAX_SUBTOTAL'])
        # print('COMMISSION   ', row['COMMISSION'])
        # print('COMMISSION_TAX_AMOUNT   ', row['COMMISSION_TAX_AMOUNT'])
        # print('')
        # print('MARKETING_FEES   ', row['MARKETING_FEES'])
        # print('STAFF_TIP   ', row['STAFF_TIP'])
        # print('CREDIT   ', row['CREDIT'])
        # print('DEBIT   ', row['DEBIT'])
        # print('')
        # print('DOORDASH_TRANSACTION_ID   ', row['DOORDASH_TRANSACTION_ID'])
        # print('PAYOUT_ID   ', row['PAYOUT_ID'])
        # print('DRIVE_CHARGE   ', row['DRIVE_CHARGE'])
        # print('TAX_REMITTED_BY_DOORDASH_TO_STATE   ', row['TAX_REMITTED_BY_DOORDASH_TO_STATE'])

        # print(row['TOTAL_BEFORE_ADJUSTMENTS'])
        # print(row['ESTIMATED_PAYOUT'])






# Doordash row headers/key names....

#"TIMESTAMP_UTC_TIME","TIMESTAMP_UTC_DATE","TIMESTAMP_LOCAL_TIME",
#"TIMESTAMP_LOCAL_DATE","PAYOUT_TIME","PAYOUT_DATE","STORE_ID",
#"BUSINESS_ID","STORE_NAME","MERCHANT_STORE_ID","TRANSACTION_TYPE",
#"TRANSACTION_ID","DOORDASH_ORDER_ID","MERCHANT_DELIVERY_ID","EXTERNAL_ID",
#"DESCRIPTION","FINAL_ORDER_STATUS","CURRENCY","SUBTOTAL","TAX_SUBTOTAL",
#"COMMISSION","COMMISSION_TAX_AMOUNT","MARKETING_FEES","STAFF_TIP",
#"CREDIT","DEBIT","DOORDASH_TRANSACTION_ID","PAYOUT_ID",
#"DRIVE_CHARGE","TAX_REMITTED_BY_DOORDASH_TO_STATE"



# ======= an ubereats file =======
# with open('ubereats_sample.csv') as file:
#     reader = csv.DictReader(file)


    # for row in reader:



    #     print('')
    #
    #
    #     print(row['Order Date / Refund date'])
    #     print(row['Food sales (including tax)'])
    #     print(row['Food Sales (excluding tax)'])
    #     print(row['Tax on Food Sales'])




# UberEats row headers/key names....

#Store Name,Store ID,Order ID,Workflow ID,Dining Mode,Order Channel,
# Order Status,Order Date / Refund date,Order Accept Time,Food Sales (excluding tax),
# Tax on Food Sales,Food sales (including tax),Adjustments (excluding tax),Tax on Adjustments,
# Promo Spend on food,Tax on Promotion on Food,Special Offer - Delivery,
# Tax on Special Offer - Delivery,Bag Fee,Marketing Service Fee Adjustment,
# Total Sales after Adjustments (including tax),Uber Service Fee,Delivery Network Fee,
# Order Processing Fee,Merchant Fee,Tax on Merchant Fee,Gratuity,Misc Payment Description,
# Miscellaneous Payments,Marketplace Facilitator Tax,Backup Withholding Tax,Payout,
# Payout Date,Markup Amount,Markup Tax,Service Fee %



# ======= a grubhub file =======
row = {'id': 1, 'date': '04/30/2021 04:00 PM', 'vendor': 'Grubhub', 'wholesale': 'true', 'subtotal': 11.0, 'tax': 1.13, 'fee': -0.67, 'commission': -1.65, 'tip': 0.0, 'unique_id': 'O-899314996514160'}
print(row['date'])
slice_object = slice(10)
sliced_date = row['date'][slice_object]

grubhub_formatted = datetime.strptime(sliced_date, '%m/%d/%Y').strftime('%Y-%m-%d')

print(grubhub_formatted)

# with open('grubhub_sample.csv') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print('')
#
#
#         print(row['Date'])
#         print(row['Subtotal'])
#         print(row['Tax'])
#         print(row['Restaurant Total'])


# Grubhub row headers/key names.....

# "ID","Restaurant","Type","Description","Date","Time","Subtotal","Service","Delivery",
# "Tax","Tip","Restaurant Total","Commission","Delivery Commission",
# "Processing Fee","Withheld Tax","Targeted Promotion"


# ======= a kioskbuddy file =======
# with open('kb_sample.csv') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print('')
#
#
#         print(row['Date'])
#         print(float(row['Subtotal']))
#         print(row['Taxes'])
#         print(row['Tips'])


# KioskBuddy row headers/key names.....

# Date,Name,Order,Number of Items,Subtotal,Taxes,Discount,Promo Code,Tips,
# Total,Transaction Client ID,Transaction ID,Location,
# Checkout Step: Order Name


# ======= a postmates file =======
# with open('postmates_sample.csv') as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         # print('')
#         #
#         #
#         # print(row['Date'])
#         # print(row['Subtotal'])
#         # print(row['Tax'])
#         # print(row['Total'])
#         date = row['Date']
#         subtotal = row['Subtotal']
#         tax = row['Tax']
#         report = {'Date': date, 'Subtotal': subtotal, 'Tax': tax}
#         print(report)



# Postmates row headers/key names.....

# Date,Place Nickname,Place Address,Order Type,Order Number,Order State,
# Customer Name,Subtotal,Tax,Fees,Total,Commission,Gift Card Redemptions,
# Adjustments,Reimbursements,Returns,Promotion Cost,Payout,Items,Issues,
# Special Instructions,Substitution,Uber Eats UUID
#----CREATE (upload) REPORTS-----
# @reports.route('/<file>', methods=['POST'])
# pass in a parameter here that is the file?


# def upload_report(file):
#     # control flow of which files so all type of files get same cutom fields
#     first_read = csv.DictReader(open(file))
#     unique_key = first_read.fieldnames[4]
#     #===== DOORDASH =====
#     if unique_key == 'Order':
#         DATE='\ufeffDate'
#         VENDOR='Doordash'
#         WHOLESALE='true'
#         SUBTOTAL='Subtotal'
#         TAX='Tax'
#         FEE='Fees'
#         COMMISSION='Commission'
#         TIP='Tip'
#     #===== GRUBHUB =====
#     if unique_key == 'Date':
#         DATE='Date'
#         VENDOR='Grubhub'
#         WHOLESALE='true'
#         SUBTOTAL='Subtotal'
#         TAX='Tax'
#         FEE='Processing Fee'
#         COMMISSION='Commission'
#         TIP='Tip'
#     # #===== UBEREATS =====
#     if unique_key == 'Dining Mode':
#         DATE='Order Date / Refund date'
#         VENDOR='UberEats'
#         WHOLESALE='true'
#         SUBTOTAL='Food Sales (excluding tax)'
#         TAX='Tax on Food Sales'
#         FEE='Order Processing Fee'
#         COMMISSION='Uber Service Fee'
#         TIP='Gratuity'
#     # #===== KIOSKBUDDY =====
#     if unique_key == 'Subtotal':
#         DATE='Date'
#         VENDOR='KioskBuddy'
#         WHOLESALE='false'
#         SUBTOTAL='Subtotal'
#         TAX='Taxes'
#         FEE='Promo Code' # This is a problem, Kioskbuddy has no fees or commision
#         COMMISSION='Discount' # These 2 fields are ti fill in the gaps
#         TIP='Tips'
#     # #===== POSTMATES =====
#     if unique_key == 'Order Number':
#         DATE='Date'
#         VENDOR='Postmates'
#         WHOLESALE='false'
#         SUBTOTAL='Subtotal'
#         TAX='Tax'
#         FEE='Fees'
#         COMMISSION='Commission'
#         TIP='Reimbursements' # same prob, no tips from PM, filled the gap



    # iterate here, had to hard code file name
    # with open(file) as file:
    #     reader = csv.DictReader(file)
    #
    #     for row in reader:
    #         uploaded_report = models.Report.create(
    #             date=row[DATE],
    #             vendor=VENDOR,
    #             wholesale=WHOLESALE,
    #             subtotal=row[SUBTOTAL],
    #             tax=row[TAX],
    #             fee=row[FEE],
    #             commission=row[COMMISSION],
    #             tip=row[TIP]
    #         )
    #
    #         report_dict = model_to_dict(uploaded_report)
    #
    #         print(report_dict)
    #
    # return jsonify(
    #     data = report_dict,
    #     message = 'Successfully uploaded report!',
    #     status = 201
    # ), 201
