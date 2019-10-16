#!/usr/bin/python3
import pymysql

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="billing_mgmt"
)

mycursor = mydb.cursor()
serial_number = 0
option = int(input("Select an option 1.Customer\n2.Admin"))
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
    if flag == 1:
        print("Item Available")
    if flag==2:
        print("Item Not Available.\nPlease select available item")
        continue


    select_quantity = int(input("Enter Quantity of Selected Item"))
    k = (select_item_id)
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
    mycursor.execute("update Menu set Available_quantity = '%d' where Item_ID ='%d'"%(new_ava_qua,select_item_id))
    choice = int(input("Do you eant to continue ?\n1.Yes\n2.Done"))
    if choice==1:
        continue
    
    if choice ==2:
        print("Selected Items:")
        for x in total_list:
            print(x)
        print("The Total Amount is :",amount)
        con =int(input("Do you want confirm order ?\n1.Confirm\n2.Edit"))
    if con==1:
        serial_number=serial_number+1
        p=str(serial_number)
        print("order number ",p.zfill(4))
        mycursor.execute("Insert into bill (item_id,total_amt) values (%d,%d)"%(select_item_id,amount))
        #mydb.commit()
        break
    elif con==2:
        continue

if option == 2:
    passw = input("Enter password")
    if passw == "password":
        print("login Successfull")
        order_no = int(input("Enter order number: "))
        mycursor.execute("select * from bill where serial_id ='%d'"%(order_no))
        select_list = list(mycursor.fetchall())
        print(select_list)



