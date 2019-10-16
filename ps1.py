#!/usr/bin/python3
import pymysql
import getpass
# Open database connection
mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="billing_mgmt"
)
# prepare a cursor object using cursor() method
mycursor = mydb.cursor()
serial_number = 0

#Menu for customer
option = int(input("Select an option 1.Customer\n2.Admin\n"))
total_list=[]
amount = 0
k=0
if(option==1):
    cust_name = input("Enter Customer name : ")
    print("Menu")
    mycursor.execute("select * from Menu")
    items=mycursor.fetchall()
    for item in items:
        print(item)

while option==1:
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
    #Checking If item exists
    if flag == 1:
        print("Item Available")
    if flag==2:
        print("Item Not Available.\nPlease select available item")
        continue


    select_quantity = int(input("Enter Quantity of Selected Item"))
    k = (select_item_id)
    # execute SQL query using execute() method.
    mycursor.execute("select Available_quantity from Menu where Item_ID ='%d'"%(select_item_id))
    select_row = list(mycursor.fetchone())
    qua_flag=1
    
    if int(select_row[0]) < select_quantity:
        qua_flag=2

    if qua_flag == 2 :
        print("Selected Quantity abone limit.\n Please select with in limit")
        continue
    
    mycursor.execute("select * from Menu where Item_ID ='%d'"%(select_item_id))
    select_list = list(mycursor.fetchall())
    #print(select_list)
    print(select_list[0][1],select_list[0][2])
    amount = amount + int(select_list[0][2])*select_quantity
    k=k+1
    total_list.append(select_list)
    new_ava_qua = select_row[0] - select_quantity
    print(new_ava_qua)
    # execute SQL query using execute() method.
    mycursor.execute("update Menu set Available_quantity = '%d' where Item_ID ='%d'"%(new_ava_qua,select_item_id))
    choice = int(input("Do you eant to continue ?\n1.Yes\n2.Done\n"))
    if choice==1:
        continue
    
    if choice ==2:
        print("Selected Items:")
        for x in total_list:
            print(x)
        print("The Total Amount is :",amount)
        con =int(input("Do you want confirm order ?\n1.Confirm\n2.Edit\n"))
    #Confirmation Block
    if con==1:
        serial_number=serial_number+1
        p=str(serial_number)
        print("order number ",p.zfill(4))
        # execute SQL query using execute() method.
        mycursor.execute("Insert into bill (item_id,total_amt,nmae) values (%d,%d,'%s')"%(select_item_id,amount,cust_name))
        #mydb.commit()
        break
    elif con==2:
        continue
#Admin Block
if option == 2:
    print("Enter password")
    passw = getpass.getpass()
    if passw == "password":
        print("login Successfull")
        order_no = int(input("Enter order number: "))
        # execute SQL query using execute() method.
        mycursor.execute("select * from bill where serial_id ='%d'"%(order_no))
        select_list = list(mycursor.fetchall())
        print(select_list)

days = input("Enter number of days\n")
mycursor.execute("select time from bill where time between '2019-10-15' and '2019-10-10'")
date = list(mycursor.fetchall())
#Calculating total amount in days
mycursor.execute("select SUM(total_amt) from bill")
t_a = list(mycursor.fetchall())
print("Total amount in last", days,"day is",t_a[0])


