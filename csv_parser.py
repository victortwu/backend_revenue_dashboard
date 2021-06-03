import csv
from datetime import datetime
import os

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
#
# date_range_str = 'Thu Apr 01 2021 00:00:00 GMT-0700 (Pacific Daylight Time),Wed Apr 14 2021 00:00:00 GMT-0700 (Pacific Daylight Time)'
# %a %b %d %Y %X %Z

# split_dates = date_range.replace(",", '","')
#
# make_list = [split_dates]
# print(len(make_list))
# print(type(make_list))
# date_range_list = date_range_str.split(',')
# print(len(date_range_list))
# print(type(date_range_list))
# print(date_range_list)
# print(type(date_range_list[0]))
# print(date_range_list[1])
#
#
# slice_object = slice(15)
# sliced_date = date_range_list[0][slice_object]
#
#
#
# formatted = datetime.strptime(sliced_date, '%a %b %d %Y').strftime('%Y-%m-%d')
# print('Here is formatted: ', formatted)

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
# with open('csv_files/ubereats_sample.csv') as file:
#     reader = csv.DictReader(file)
#
#
#     for row in reader:
#
#
#
#         print('')
#
#         print('commissions-----')
#         print(row['Uber Service Fee'])
#         print('fee------')
#         print(row['Merchant Fee'])
        # print(row['Food Sales (excluding tax)'])
        # print(row['Tax on Food Sales'])




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
# row = {'id': 1, 'date': '04/30/2021 04:00 PM', 'vendor': 'Grubhub', 'wholesale': 'true', 'subtotal': 11.0, 'tax': 1.13, 'fee': -0.67, 'commission': -1.65, 'tip': 0.0, 'unique_id': 'O-899314996514160'}
# print(row['date'])
# slice_object = slice(10)
# sliced_date = row['date'][slice_object]
#
# grubhub_formatted = datetime.strptime(sliced_date, '%m/%d/%Y').strftime('%Y-%m-%d')
#
# print(grubhub_formatted)

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

# here = os.getcwd()

# file_path = os.path.relpath(here + 'postmates_two_weeks.csv')
# print(file_path+'/'+'postmates_two_weeks.csv')
# whole_rel_path = file_path+'/'+'postmates_two_weeks.csv'
# # # os.chdir(here)
# whole_file_path = os.path.join('~'+here, 'postmates_two_weeks.csv')
# print(whole_file_path)
# print(os.path.abspath('./postmates_two_weeks.csv'))
# absolute_path = os.path.abspath('./postmates_two_weeks.csv')
#
whats_this = b"Date,Place Nickname,Place Address,Order Type,Order,Order State,Customer Name,API Delivery Fee,Tip,API Delivery Total,Subtotal,Tax,Fees,Total,Commission,Gift Card Redemptions,Adjustments,Reimbursement,Returns,Promotion Cost,Payout,items,Issues,Special Instructions,Substitution\r\nMon May 17 2021 12:42:54 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,897,Completed,Gautham G.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken D\xc3\xb6ner Sandwiches: Chicken Scorching Kreuzberg (Bread?: Pita Wrap; Extras?: Add Extra Meat); 0 x Set of utensils,None,,\r\nThu May 13 2021 12:04:39 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,896,Completed,Murphy R.,$0.00,$0.00,$0.00,$10.00,$1.01,$0.00,$11.01,($1.50),$0.00,$0.00,$0.00,$0.00,$0.00,$9.51,Vegetarian D\xc3\xb6ner Sandwiches: Tofu & Feta Berliner (Bread?: Pita Wrap; Extras?: Add Extra Sauce); 0 x Set of utensils,None,,\r\nThu May 13 2021 12:00:30 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,895,Completed,Yaw N.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Drinks: Bottle of Water; Chicken D\xc3\xb6ner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nWed May 12 2021 18:44:20 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,894,Completed,shuai c.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,Chicken D\xc3\xb6ner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended)); Chicken D\xc3\xb6ner Sandwiches: House Chicken (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nWed May 12 2021 14:30:02 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,893,Completed,amit s.,$0.00,$0.00,$0.00,$26.50,$2.68,$0.00,$29.18,($3.97),$0.00,$0.00,$0.00,$0.00,$0.00,$25.21,Entr\xc3\xa9e Salads: Berliner Chicken Salad (Anything you DON'T want on it?: No Feta Cheese (if applicable); Extras?: Add Extra Meat); Entr\xc3\xa9e Salads: Fiery Kreuzberg Chicken Salad (Extras?: Add Extra Sauce); 0 x Set of utensils,None,,\r\nWed May 12 2021 13:49:51 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,892,Completed,Bobby H.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken D\xc3\xb6ner Sandwiches: Chicken Scorching Kreuzberg (Extras?: Add Extra Meat; Bread?: Spinach Tortilla); 0 x Set of utensils,None,,\r\nTue May 11 2021 13:49:28 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,891,Completed,Ankit G.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Entr\xc3\xa9e Salads: Fiery Kreuzberg Chicken Salad; 0 x Set of utensils,None,,\r\nTue May 11 2021 12:59:20 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,890,Completed,Leslie B.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Chicken D\xc3\xb6ner Sandwiches: Chicken Fiery Kreuzberg (Extras?: Add Extra Sauce; Add Feta Cheese; Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nTue May 11 2021 12:22:20 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,889,Completed,Arpit K.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,2 x Chicken D\xc3\xb6ner Sandwiches: House Chicken (Bread?: Pita Wrap); 0 x Set of utensils,None,,\r\nMon May 10 2021 12:58:30 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,888,Completed,Bobby H.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken D\xc3\xb6ner Sandwiches: Chicken Scorching Kreuzberg (Extras?: Add Extra Meat; Bread?: Spinach Tortilla); 0 x Set of utensils,None,,\r\nMon May 10 2021 12:39:05 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,887,Completed,Tim C.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Lamb and Beef D\xc3\xb6ner Sandwiches: House Lamb and Beef (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nMon May 10 2021 12:37:31 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,886,Completed,XIV T.,$0.00,$0.00,$0.00,$37.00,$3.74,$0.00,$40.74,($5.55),$0.00,$0.00,$0.00,$0.00,$0.00,$35.19,Lamb and Beef D\xc3\xb6ner Sandwiches: House Lamb and Beef (Bread?: House Bread (recommended); Extras?: Side of Hot Sauce); Entr\xc3\xa9e Salads: Fiery Kreuzberg Chicken Salad (Extras?: Side of Hot Sauce); Lamb and Beef D\xc3\xb6ner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended); Anything you DON'T want on it?: No Tomatoes; No Cucumbers); 0 x Set of utensils,None,,\r\nMon May 10 2021 12:04:25 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,885,Completed,Mark K.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,Chicken D\xc3\xb6ner Sandwiches: House Chicken (Bread?: House Bread (recommended)); Chicken D\xc3\xb6ner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nMon May 10 2021 11:38:11 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,884,Completed,Kevin G.,$0.00,$0.00,$0.00,$15.50,$1.57,$0.00,$17.07,($2.32),$0.00,$0.00,$0.00,$0.00,$0.00,$14.75,Drinks: Can of Coke; Chicken D\xc3\xb6ner Sandwiches: Chicken Fiery Kreuzberg (Bread?: Spinach Tortilla; Extras?: Add Extra Meat); 0 x Set of utensils,None,,\r\nThu May 06 2021 19:34:19 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,883,Completed,Sarah F.,$0.00,$0.00,$0.00,$68.00,$6.87,$0.00,$74.87,($10.20),$0.00,$0.00,$0.00,$0.00,$0.00,$64.67,D\xc3\xb6ner Platters: Lamb and Beef Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce; Anything you DON'T want on it?: No Tofu (if applicable); No Tomatoes; No Cucumbers; No Red Cabbage); 3 x D\xc3\xb6ner Platters: Lamb and Beef Platter; Lamb and Beef D\xc3\xb6ner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nThu May 06 2021 16:47:18 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,882,Completed,Stacey G.,$0.00,$0.00,$0.00,$11.00,$1.11,$0.00,$12.11,($1.65),$0.00,$0.00,$0.00,$0.00,$0.00,$10.46,Chicken D\xc3\xb6ner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended); Extras?: Add Extra Sauce); 0 x Set of utensils,None,,\r\nWed May 05 2021 19:30:53 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,881,Completed,fardin r.,$0.00,$0.00,$0.00,$37.00,$3.74,$0.00,$40.74,($5.55),$0.00,$0.00,$0.00,$0.00,$0.00,$35.19,D\xc3\xb6ner Platters: Chicken Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 2 x Lamb and Beef D\xc3\xb6ner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nWed May 05 2021 17:39:37 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Delivery,880,Completed,Austin H.,$0.00,$0.00,$0.00,$24.00,$2.42,$0.00,$26.42,($3.60),$0.00,$0.00,$0.00,$0.00,$0.00,$22.82,Chicken D\xc3\xb6ner Sandwiches: House Chicken (Bread?: House Bread (recommended)); D\xc3\xb6ner Platters: Chicken Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 0 x Set of utensils,None,,\r\nTue May 04 2021 11:45:17 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,879,Completed,Mark K.,$0.00,$0.00,$0.00,$11.00,$1.11,$0.00,$12.11,($1.65),$0.00,$0.00,$0.00,$0.00,$0.00,$10.46,Chicken D\xc3\xb6ner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,\r\nMon May 03 2021 13:17:01 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,878,Completed,Sean H.,$0.00,$0.00,$0.00,$14.00,$1.41,$0.00,$15.41,($2.10),$0.00,$0.00,$0.00,$0.00,$0.00,$13.31,D\xc3\xb6ner Platters: Lamb and Beef Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 0 x Set of utensils,None,,\r\nMon May 03 2021 12:09:25 GMT-0700 (Pacific Daylight Time),The Berliner D\xc3\xb6ner Kebab Seattle,428 Westlake Ave N,Pickup,877,Completed,Ryan C.,$0.00,$0.00,$0.00,$25.50,$2.58,$0.00,$28.08,($3.82),$0.00,$0.00,$0.00,$0.00,$0.00,$24.26,Chicken D\xc3\xb6ner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended)); Lamb and Beef D\xc3\xb6ner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended); Extras?: Add Extra Meat); 0 x Set of utensils,None,,\r\n"

rawtext = """Date,Place Nickname,Place Address,Order Type,Order,Order State,Customer Name,API Delivery Fee,Tip,API Delivery Total,Subtotal,Tax,Fees,Total,Commission,Gift Card Redemptions,Adjustments,Reimbursement,Returns,Promotion Cost,Payout,items,Issues,Special Instructions,Substitution
Mon May 17 2021 12:42:54 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,897,Completed,Gautham G.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken Döner Sandwiches: Chicken Scorching Kreuzberg (Bread?: Pita Wrap; Extras?: Add Extra Meat); 0 x Set of utensils,None,,
Thu May 13 2021 12:04:39 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,896,Completed,Murphy R.,$0.00,$0.00,$0.00,$10.00,$1.01,$0.00,$11.01,($1.50),$0.00,$0.00,$0.00,$0.00,$0.00,$9.51,Vegetarian Döner Sandwiches: Tofu & Feta Berliner (Bread?: Pita Wrap; Extras?: Add Extra Sauce); 0 x Set of utensils,None,,
Thu May 13 2021 12:00:30 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,895,Completed,Yaw N.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Drinks: Bottle of Water; Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Wed May 12 2021 18:44:20 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,894,Completed,shuai c.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,Chicken Döner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended)); Chicken Döner Sandwiches: House Chicken (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Wed May 12 2021 14:30:02 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,893,Completed,amit s.,$0.00,$0.00,$0.00,$26.50,$2.68,$0.00,$29.18,($3.97),$0.00,$0.00,$0.00,$0.00,$0.00,$25.21,Entrée Salads: Berliner Chicken Salad (Anything you DON'T want on it?: No Feta Cheese (if applicable); Extras?: Add Extra Meat); Entrée Salads: Fiery Kreuzberg Chicken Salad (Extras?: Add Extra Sauce); 0 x Set of utensils,None,,
Wed May 12 2021 13:49:51 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,892,Completed,Bobby H.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken Döner Sandwiches: Chicken Scorching Kreuzberg (Extras?: Add Extra Meat; Bread?: Spinach Tortilla); 0 x Set of utensils,None,,
Tue May 11 2021 13:49:28 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,891,Completed,Ankit G.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Entrée Salads: Fiery Kreuzberg Chicken Salad; 0 x Set of utensils,None,,
Tue May 11 2021 12:59:20 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,890,Completed,Leslie B.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Extras?: Add Extra Sauce; Add Feta Cheese; Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Tue May 11 2021 12:22:20 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,889,Completed,Arpit K.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,2 x Chicken Döner Sandwiches: House Chicken (Bread?: Pita Wrap); 0 x Set of utensils,None,,
Mon May 10 2021 12:58:30 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,888,Completed,Bobby H.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken Döner Sandwiches: Chicken Scorching Kreuzberg (Extras?: Add Extra Meat; Bread?: Spinach Tortilla); 0 x Set of utensils,None,,
Mon May 10 2021 12:39:05 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,887,Completed,Tim C.,$0.00,$0.00,$0.00,$12.00,$1.21,$0.00,$13.21,($1.80),$0.00,$0.00,$0.00,$0.00,$0.00,$11.41,Lamb and Beef Döner Sandwiches: House Lamb and Beef (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Mon May 10 2021 12:37:31 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,886,Completed,XIV T.,$0.00,$0.00,$0.00,$37.00,$3.74,$0.00,$40.74,($5.55),$0.00,$0.00,$0.00,$0.00,$0.00,$35.19,Lamb and Beef Döner Sandwiches: House Lamb and Beef (Bread?: House Bread (recommended); Extras?: Side of Hot Sauce); Entrée Salads: Fiery Kreuzberg Chicken Salad (Extras?: Side of Hot Sauce); Lamb and Beef Döner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended); Anything you DON'T want on it?: No Tomatoes; No Cucumbers); 0 x Set of utensils,None,,
Mon May 10 2021 12:04:25 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,885,Completed,Mark K.,$0.00,$0.00,$0.00,$22.00,$2.22,$0.00,$24.22,($3.30),$0.00,$0.00,$0.00,$0.00,$0.00,$20.92,Chicken Döner Sandwiches: House Chicken (Bread?: House Bread (recommended)); Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Mon May 10 2021 11:38:11 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,884,Completed,Kevin G.,$0.00,$0.00,$0.00,$15.50,$1.57,$0.00,$17.07,($2.32),$0.00,$0.00,$0.00,$0.00,$0.00,$14.75,Drinks: Can of Coke; Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Bread?: Spinach Tortilla; Extras?: Add Extra Meat); 0 x Set of utensils,None,,
Thu May 06 2021 19:34:19 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,883,Completed,Sarah F.,$0.00,$0.00,$0.00,$68.00,$6.87,$0.00,$74.87,($10.20),$0.00,$0.00,$0.00,$0.00,$0.00,$64.67,Döner Platters: Lamb and Beef Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce; Anything you DON'T want on it?: No Tofu (if applicable); No Tomatoes; No Cucumbers; No Red Cabbage); 3 x Döner Platters: Lamb and Beef Platter; Lamb and Beef Döner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Thu May 06 2021 16:47:18 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,882,Completed,Stacey G.,$0.00,$0.00,$0.00,$11.00,$1.11,$0.00,$12.11,($1.65),$0.00,$0.00,$0.00,$0.00,$0.00,$10.46,Chicken Döner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended); Extras?: Add Extra Sauce); 0 x Set of utensils,None,,
Wed May 05 2021 19:30:53 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,881,Completed,fardin r.,$0.00,$0.00,$0.00,$37.00,$3.74,$0.00,$40.74,($5.55),$0.00,$0.00,$0.00,$0.00,$0.00,$35.19,Döner Platters: Chicken Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 2 x Lamb and Beef Döner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Wed May 05 2021 17:39:37 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Delivery,880,Completed,Austin H.,$0.00,$0.00,$0.00,$24.00,$2.42,$0.00,$26.42,($3.60),$0.00,$0.00,$0.00,$0.00,$0.00,$22.82,Chicken Döner Sandwiches: House Chicken (Bread?: House Bread (recommended)); Döner Platters: Chicken Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 0 x Set of utensils,None,,
Tue May 04 2021 11:45:17 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,879,Completed,Mark K.,$0.00,$0.00,$0.00,$11.00,$1.11,$0.00,$12.11,($1.65),$0.00,$0.00,$0.00,$0.00,$0.00,$10.46,Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,
Mon May 03 2021 13:17:01 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,878,Completed,Sean H.,$0.00,$0.00,$0.00,$14.00,$1.41,$0.00,$15.41,($2.10),$0.00,$0.00,$0.00,$0.00,$0.00,$13.31,Döner Platters: Lamb and Beef Platter (Garlic Sauce; Dill Yogurt Sauce or House Hot Sauce?: Garlic Sauce); 0 x Set of utensils,None,,
Mon May 03 2021 12:09:25 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,877,Completed,Ryan C.,$0.00,$0.00,$0.00,$25.50,$2.58,$0.00,$28.08,($3.82),$0.00,$0.00,$0.00,$0.00,$0.00,$24.26,Chicken Döner Sandwiches: Chicken Berliner (Bread?: House Bread (recommended)); Lamb and Beef Döner Sandwiches: Lamb and Beef Berliner (Bread?: House Bread (recommended); Extras?: Add Extra Meat); 0 x Set of utensils,None,,"""



data = 'Date,Place Nickname,Place Address,Order Type,Order,Order State,Customer Name,API Delivery Fee,Tip,API Delivery Total,Subtotal,Tax,Fees,Total,Commission,Gift Card Redemptions,Adjustments,Reimbursement,Returns,Promotion Cost,Payout,items,Issues,Special Instructions,Substitution\nMon May 17 2021 12:42:54 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,897,Completed,Gautham G.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Chicken Döner Sandwiches: Chicken Scorching Kreuzberg (Bread?: Pita Wrap; Extras?: Add Extra Meat); 0 x Set of utensils,None,,Thu May 13 2021 12:04:39 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,896,Completed,Murphy R.,$0.00,$0.00,$0.00,$10.00,$1.01,$0.00,$11.01,($1.50),$0.00,$0.00,$0.00,$0.00,$0.00,$9.51,Vegetarian Döner Sandwiches: Tofu & Feta Berliner (Bread?: Pita Wrap; Extras?: Add Extra Sauce); 0 x Set of utensils,None,,Thu May 13 2021 12:00:30 GMT-0700 (Pacific Daylight Time),The Berliner Döner Kebab Seattle,428 Westlake Ave N,Pickup,895,Completed,Yaw N.,$0.00,$0.00,$0.00,$13.50,$1.36,$0.00,$14.86,($2.02),$0.00,$0.00,$0.00,$0.00,$0.00,$12.84,Drinks: Bottle of Water; Chicken Döner Sandwiches: Chicken Fiery Kreuzberg (Bread?: House Bread (recommended)); 0 x Set of utensils,None,,'
# print(type(whats_this))

string = whats_this.decode('utf-8')

print(type(string))


# data_to_read = rawtext.splitlines()
#
first_read = csv.DictReader(string.splitlines())
unique_key = first_read.fieldnames[4]
print(unique_key)


reader = csv.DictReader(string.splitlines())
#
#
#
for row in reader:
    print(row['Date'])

# print(data)
#
#
# with open(data) as file:
#     reader = csv.DictReader(file)
#
#     for row in reader:
#         print(row)
#         #
#         #
        # print('Commission----')
        # print(row['Commission'])
        # print('Fees-----')
        # print(row['Fees'])
        # date = row['Date']
        # subtotal = row['Subtotal']
        # tax = row['Tax']
#         report = {'Date': date, 'Subtotal': subtotal, 'Tax': tax}
#         print(report)
# file_path = os.path.relpath(here, 'postmates_two_weeks.csv')
# print(file_path)

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
