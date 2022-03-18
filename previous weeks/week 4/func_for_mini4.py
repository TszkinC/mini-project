import pandas as pd

product_csv=pd.read_csv("product.csv")
courier_csv=pd.read_csv("courier.csv")
orders_csv=pd.read_csv("orders.csv")
status_list={1:"preparing", 2:"out for delivery",3:"done"}

#function to add item to product list
def add_product():
    """function to add new item to product list"""
    item=input ("What would you like to add?\n")
    price=input("Please input its price\n")
    col_name=["name", "price"]
    data1={"name": item,"price": float(price)}
    new_row=pd.DataFrame(data1, columns=col_name, index=[0])
    new_row.to_csv("product.csv",mode="a", index=False,header=False)

#function to update product list
def update_product():
    """function to update product list"""
    print(product_csv)
    while True:
        product_to_update=input("Please input the index of the product to be updated\n")
        if product_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_price=input("Enter the new price\n")
            product_csv.loc[[int(product_to_update)], ['price']] = float(new_price)
            product_csv.to_csv("product.csv", index=False)
            break
    
#function to delete item from product list
def delete_product():
    """function to delete an item from product list"""
    print(product_csv)
    while True:
        product_to_delete=input("Please input the index of the product to be deleted\n")
        if product_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            product_csv.drop(int(product_to_delete), axis=0, inplace=True)
            product_csv.to_csv("product.csv", index=False)
            break

#function to add courier
def add_courier():
    """function to add new item to courier list"""
    courier=input ("What would you like to add?\n")
    phone=input("Please input its phone no.\n")
    col_name=["name", "phone"]
    data2={"name": courier,"phone": phone}
    new_row=pd.DataFrame(data2, columns=col_name, index=[0])
    new_row.to_csv("courier.csv",mode="a", index=False,header=False)


#function to update courier
def update_courier():
    """function to update courier list"""
    print(courier_csv)
    while True:
        courier_to_update=input("Please input the index of the courier to be updated\n")
        if courier_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_phone=input("Enter the new phone no.\n")
            courier_csv.loc[[int(courier_to_update)], ['phone']]=new_phone
            courier_csv.to_csv("courier.csv", index=False)
            break
    
#function to delete courier
def delete_courier():
    """function to delete an item from courier list"""
    print(courier_csv)
    while True:
        courier_to_delete=input("Please input the index of the product to be deleted\n")
        if courier_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            courier_csv.drop(int(courier_to_delete), axis=0, inplace=True)
            courier_csv.to_csv("courier.csv", index=False)
            break
    
# function to add new order
def add_new_order():
    cus_name=input("Please input customer's name\n")
    cus_add=input("Please input customer's address\n")
    cus_phone=input("Please input customer's phone number\n")
    print(product_csv)
    cus_product=int(input("Please choose a product by index\n"))
    x=product_csv.loc[cus_product,"name"]
    print(courier_csv)
    cus_courier=int(input("Please choose a courier by index\n"))
    y=courier_csv.loc[cus_courier,"name"]
    cus_status=input("Please choose the index of customer's status, \n1--preparing \n2--out for delivery \n3--done\n")
    col_name=["cus_name", "cus_add", "cus_phone", "cus_product", "courier", "status"]
    data3={"cus_name": cus_name, "cus_add": cus_add, "cus_phone":cus_phone, "cus_product":x, "courier":y, "status":status_list[int(cus_status)]}
    new_row=pd.DataFrame(data3, columns=col_name, index=[0])
    new_row.to_csv("orders.csv",mode="a", index=False,header=False)

#function to update order status    
def update_order_status():
    """function to update courier list"""
    print(orders_csv)
    while True:
        order_to_update=input("Please input the index of the order to be updated\n")
        if order_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            new_status=input("Please choose the index of customer's status, \n1--preparing \n2--out for delivery \n3--done\n")
            orders_csv.loc[[int(order_to_update)], ['status']]=status_list[int(new_status)]
            orders_csv.to_csv("orders.csv", index=False)
            break

#function to update order detail    
def update_order_detail():
    """function to order detail"""
    while True:
        print(orders_csv.iloc[:,[0,1,2,3,4]])
        order_to_update=input("Please input the index of the order to be updated\n")
        if order_to_update=="":
            print ("Wrong input. Please try again!\n")
        else:
            detail_to_update = int(input("Please choose the index of detail to update, 1--customer name \n2--customer address \n3--contact no. \n4--product chosen \n5--courier \n0--exit\n"))
            if detail_to_update==0:
                break
            elif detail_to_update=="":
                print ("Wrong input. Please try again!\n")
            elif detail_to_update==1:
                new_cus_name=input("Please input the new customer name\n")
                orders_csv.iloc[[int(order_to_update)], [int(detail_to_update)-1]]=new_cus_name
                orders_csv.to_csv("orders.csv", index=False)
                break
            elif detail_to_update==2:
                new_add=input("Please input the new address\n")
                orders_csv.iloc[[int(order_to_update)], [int(detail_to_update)-1]]=new_add
                orders_csv.to_csv("orders.csv", index=False)
                break
            elif detail_to_update==3:
                new_number=input("Please input the new contact no.\n")
                orders_csv.iloc[[int(order_to_update)], [int(detail_to_update)-1]]=new_number
                orders_csv.to_csv("orders.csv", index=False)
                break
            elif detail_to_update==4:
                print (product_csv)
                new_product=input("Please input the index of the new product chosen\n")
                orders_csv.iloc[[int(order_to_update)], [int(detail_to_update)-1]]=product_csv.iloc[[int(new_product)], [0]]
                orders_csv.to_csv("orders.csv", index=False)
                break
            elif detail_to_update==5:
                print (courier_csv)
                new_courier=input("Please input the index of the new product chosen\n")
                orders_csv.iloc[[int(order_to_update)], [int(detail_to_update)-1]]=courier_csv.iloc[[int(new_courier)], [0]]
                orders_csv.to_csv("orders.csv", index=False)
                break
        
#function to delete order
def delete_order():
    """function to delete an item from courier list"""
    print(orders_csv)
    while True:
        order_to_delete=input("Please input the index of the product to be deleted\n")
        if order_to_delete=="":
            print ("Wrong input. Please try again!\n")
        else:
            orders_csv.drop(int(order_to_delete), axis=0, inplace=True)
            orders_csv.to_csv("orders.csv", index=False)
            break