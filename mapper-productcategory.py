#!/usr/bin/env python3

import sys

for line in sys.stdin:
    
    data = line.strip()
    
    if not data:
        continue
    
    if 'Customer_Id' in data:
        continue
    
    # [NOTE] handling csv file only
    cols_data = line.split(',')
    
    # wiht the squence of the column as :
    # 'Order_Date', 'Time', 'Aging', 'Customer_Id', 'Gender', 
    # 'Device_Type', 'Customer_Login_type', 'Product_Category', 
    # 'Product', 'Sales', 'Quantity', 'Discount', 'Profit', 'Shipping_Cost', 
    # 'Order_Priority','Payment_method'
    
    # [NOTE] we only need ['Sales', 'Quantity', 'Discount', 'Shipping_Cost', 'Product_Category', 'Payment_method']
    # AS THE LIST SEQUENCE INDEX IS (9, 10, 11, 13, 7, 15)
    
    try:
        sales_value = cols_data[9]
        quantity_value = cols_data[10]
        discount_value = cols_data[11]
        shipcost_value = cols_data[13]
        prodcategory_value = cols_data[7]
        paymentmethod_value = cols_data[15]
        
        accumulative_value = float(sales_value) * float(quantity_value) - float(discount_value) + float(shipcost_value)
        key = {prodcategory_value}|{paymentmethod_value}
        
        # print(f"{sales_value}|{quantity_value}|{discount_value}|{shipcost_value}|{prodcategory_value}|{paymentmethod_value}")
        # print(f"{paymentmethod_value}\t{accumulative_value}")
        print(f"{prodcategory_value}\t{accumulative_value}")
    
    except Exception as e:
        continue