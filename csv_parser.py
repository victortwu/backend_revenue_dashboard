import csv

reader = csv.DictReader(open('ubereats_sample.csv'))
print('UberEats key: ', reader.fieldnames[4])

reader = csv.DictReader(open('Deliveries.csv'))
print('Doordash key: ', reader.fieldnames[4])

reader = csv.DictReader(open('grubhub_sample.csv'))
print('Grubhub key: ', reader.fieldnames[4])

reader = csv.DictReader(open('kb_sample.csv'))
print('KioskBuddy key: ', reader.fieldnames[4])

reader = csv.DictReader(open('postmates_sample.csv'))
print('Postmates key: ', reader.fieldnames[4])



# ======== a doordash file ===========
with open('Deliveries.csv') as file:
    reader = csv.DictReader(file)

    for row in reader:
        print('')
        print(row['\ufeffDate'])
        number = float(row['Subtotal'].replace('$', ''))

        print(number)
        print(row['Commission'])
        print(row['Payout'])


# Doordash row headers/key names....

# Date,Place Nickname,Place Address,Order Type,Order,Order State,Customer Name,
# API Delivery Fee,Tip,API Delivery Total,Subtotal,Tax,Fees,Total,Commission,
# Gift Card Redemptions,Adjustments,Reimbursement,Returns,Promotion Cost,
# Payout,items,Issues,Special Instructions,Substitution



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
