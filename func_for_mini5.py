import pymysql
import tabulate
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
host = os.environ.get("mysql_host")
user = os.environ.get("mysql_user")
password = os.environ.get("mysql_pass")
database = os.environ.get("mysql_db")

status_list={1:"preparing", 2:"out for delivery",3:"done"}

# Establish a database connection
def execute_query(statement, host=host,user=user,password=password,database=database):
    """[to establish and close connection with database and execute query ]

    Args:
        statement (str): [the SQL query]
        host (str):  Defaults to host.
        user (str): Defaults to user.
        password (str): Defaults to password.
        database (str): Defaults to database.

    Returns:
        [type]: [description]
    """
    connection = pymysql.connect(host,user,password,database, autocommit=True)
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    cursor.execute(statement)
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows


#function to print table from database
def print_table(table):
    """[function to print table from database: product, courier or orders]

    Args:
        table (str): [database has 3 tables, product, courier or orders]
    """
    dataset=execute_query(f'select * from {table}')
    header=dataset[0].keys()
    rows=[x.values() for x in dataset]
    print(tabulate.tabulate(rows,header,tablefmt='rst'))
    
#function to add item to product list
def add_product():
    """function to add new item to the product table"""
    item=input("What would you like to add?\n")
    price=float(input("Please input its price\n"))
    execute_query(f"insert into product (product_name,price) values ('{item}',{price})")
    print("New product is added successfully")

#function to update product list
def update_product():
    """function to update an item in the product table"""
    print_table("product")
    while True:
        product_to_update=input("Please input the index of the product to be updated\n")
        if product_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_price=input("Enter the new price\n")
            if new_price=="":
                print ("No input. Update aborted")
                break
            else:
                execute_query(f"update product set price={new_price} where product_id={product_to_update}")
                print("Product is updated successfully")
                break
    
#function to delete item from product list
def delete_product():
    """function to delete an item from the product table"""
    print_table("product")
    while True:
        product_to_delete=input("Please input the index of the product to be deleted\n")
        if product_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            execute_query(f"delete from product where product_id={product_to_delete}")
            print("Product is deleted successfully")
            break

#function to add courier
def add_courier():
    """function to add new item to courier list"""
    courier=input ("What would you like to add?\n")
    phone=input("Please input its phone no.\n")
    execute_query(f"insert into courier (courier_name,contact_no) values ('{courier}','{phone}')")
    print("New courier is added successfully")


#function to update courier
def update_courier():
    """function to update courier list"""
    print_table("courier")
    while True:
        courier_to_update=input("Please input the index of the product to be deleted\n")
        if courier_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_phone=input("Enter the new contact no\n")
            execute_query(f"update courier set contact_no={new_phone} where courier_id={courier_to_update}")
            print("Courier is updated successfully")
            break
    
#function to delete courier
def delete_courier():
    """function to delete an item from courier list"""
    print_table("courier")
    while True:
        courier_to_delete=input("Please input the index of the product to be deleted\n")
        if courier_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            execute_query(f"delete from courier where courier_id={courier_to_delete}")
            print("Courier is deleted successfully")
            break
    
# function to add new order
def add_new_order():
    """function to add new order detail to order table
    """
    cus_name=input("Please input customer's name\n")
    cus_add=input("Please input customer's address\n")
    cus_phone=input("Please input customer's phone number\n")
    print_table("product")
    cus_product=int(input("Please choose a product by index\n"))
    list_x=execute_query(f"select product_name from product where product_id={cus_product}")
    x=list_x[0]["product_name"]
    print_table("courier")
    cus_courier=int(input("Please choose a courier by index\n"))
    list_y=execute_query(f"select courier_name from courier where courier_id={cus_courier}")
    y=list_y[0]["courier_name"]
    cus_status=input("Please choose the index of customer's status, \n1--preparing \n2--out for delivery \n3--done\n")
    execute_query(f"insert into orders (cus_name,cus_add,cus_phone_no,product,product_id,courier,courier_id,status) values ('{cus_name}','{cus_add}','{cus_phone}','{x}',{cus_product},'{y}',{cus_courier},'{status_list[int(cus_status)]}')")
    print("New order is added successfully")

#function to update order status    
def update_order_status():
    """function to update courier list"""
    print_table("orders")
    while True:
        order_to_update=input("Please input the index of the order to be updated\n")
        if order_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_status=input("Please choose the index of customer's status, \n1--preparing \n2--out for delivery \n3--done\n")
            execute_query(f"update orders set status='{status_list[int(new_status)]}' where order_id={order_to_update};")
            print("Order status is updated successfully")
            break

#function to update order detail    
def update_order_detail():
    """function to order detail"""
    while True:
        print_table("orders")
        order_to_update=input("Please input the index of the order to be updated\n")
        if order_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            detail_to_update = int(input("Please choose the index of detail to update,\n1--customer name \n2--customer address \n3--contact no. \n4--product chosen \n5--courier \n0--exit\n"))
            if detail_to_update==0:
                break
            elif detail_to_update=="":
                print ("Wrong input. Please try again!\n")
            elif detail_to_update==1:
                new_cus_name=input("Please input the new customer name\n")
                execute_query(f"update orders set cus_name='{new_cus_name}' where order_id={order_to_update};")
                print("Customer name is updated successfully")
                break
            elif detail_to_update==2:
                new_add=input("Please input the new address\n")
                execute_query(f"update orders set cus_add='{new_add}' where order_id={order_to_update};")
                print("Customer address is updated successfully")
                break
            elif detail_to_update==3:
                new_number=input("Please input the new contact no.\n")
                execute_query(f"update orders set cus_phone_no='{new_number}' where order_id={order_to_update};")
                print("Customer number is updated successfully")
                break
            elif detail_to_update==4:
                print_table("product")
                new_product=int(input("Please input the index of the new product chosen\n"))
                list_x=execute_query(f"select product_name from product where product_id={new_product}")
                x=list_x[0]["product_name"]
                execute_query(f"update orders set product='{x}' where order_id={order_to_update};")
                execute_query(f"update orders set product_id={new_product} where order_id={order_to_update};")
                print("Product chosen is updated successfully")
                break
            elif detail_to_update==5:
                print_table("courier")
                new_courier=input("Please input the index of the new product chosen\n")
                list_y=execute_query(f"select courier_name from courier where courier_id={new_courier}")
                y=list_y[0]["courier_name"]
                execute_query(f"update orders set courier='{y}' where order_id={order_to_update};")
                execute_query(f"update orders set courier_id={new_courier} where order_id={order_to_update};")
                print("Courier chosen is updated successfully")
                break
        
#function to delete order
def delete_order():
    """function to delete an item from courier list"""
    print_table("orders")
    while True:
        order_to_delete=input("Please input the index of the product to be deleted\n")
        if order_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            execute_query(f"delete from orders where order_id={order_to_delete}")
            print("Order is deleted successfully")
            break
        
#practising git push