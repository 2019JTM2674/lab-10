#!/usr/bin/python3
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="billing_mgmt"
)

mycursor = mydb.cursor()

option = int(input("Select an option 1.Customer\n2.Admin"))
while(option==1):
    cust_name = input("Enter Customer name : ")
    print("Menu")
    mycursor.execute("select * from Menu")
    items=mycursor.fetchall()
    for item in items:
        print(item)


    select_item_id = int(input("Enter Item_Id"))
    mycursor.execute("select Item_Id from Menu")
    Item_Id = mycursor.fetchall()
    Item_Id_list = [row[0] for row in Item_Id]
    #print(Item_Id_list)
    flag = 2
    for num in Item_Id_list:
        if num == select_item_id:
            flag=1
            break
    if flag == 1:
        print("Item Available")
    if flag==2:
        print("Item Not Available.\nPlease select available item")
        continue


    select_quantity = int(input("Enter Quantity of Selected Item"))
    mycursor.execute("select Available_quantity from Menu where Item_ID = '{select_item_id}'")
    select_row = mycursor.fetchone()
    print(select_row)
    for x in select_row:
        #print(x[0])
        print(x)
    # quantity = mycursor.fetchall()
    # quantity_list = [row[0] for row in quantity]
    # qua_flag=2
    # #print(quantity_list)
    # for qua in quantity_list:
    #     if qua > select_quantity:
    #         qua_flag=1
    #         break