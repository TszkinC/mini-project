import func_for_mini as fun
#LOAD products list from products.txt
#LOAD couriers list from couriers.txt
# CREATE orders list of dictionaries # WEEK 3 UPDATE
# CREATE order status list # WEEK 3 UPDATE

product=[]
with open ("product.txt","r") as f:
    read_product = f.readlines()
    for line in read_product:
        product.append(line.rstrip())

courier=[]
with open ("courier.txt","r") as j:
    read_courier = j.readlines()
    for line in read_courier:
        courier.append(line.rstrip())
        

orderlist = []
order1 = {"Order_id: 1","customer name: John", "customer address: M32 4TF", "customer phone no.: 897413156" , "customer product: coke_zero", "courier: DHL", "status: preparing"}
orderlist.append(order1)
order2 = {"Order_id: 2","customer name: Tom", "customer address: M17 4PP", "customer phone no.: 654213789" , "customer product: pasta", "courier: Amago", "status: preparing"}
orderlist.append(order2)
order_id = 2
class Orders:
    
    status_list=["preparing", "out for delivery", "done"]
    
    def __init__(self, order_id, cus_name,cus_add,cus_phone,cus_product,cus_courier,cus_status):
        self.order_id = order_id
        self.cus_name = cus_name
        self.cus_add = cus_add
        self.cus_phone = cus_phone
        self.cus_product = cus_product
        self.cus_courier = cus_courier
        self.status = cus_status
    def update_status(self):
        for i, j in enumerate(self.status_list):
            print(i, j)
        self.status = self.status_list[int(input("Select a new status: "))]


print ("Welcome to Cafe Python. What can I do for you?\n")
    
while True:
    choose_your_op1 = int(input ("\nPlease choose the service \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n3 - Order menu\n"))
    if choose_your_op1 ==0:
        f.close()
        j.close()
        print ("Thanks for visiting us!")
        break
    elif choose_your_op1 ==1:
        while True:
            choose_your_op2= int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print menu option \n2 - Create a new product \n3 - Update an existing product \n4 - Delete a product\n"))
            if choose_your_op2 == 0:
                break
            elif choose_your_op2==1:
                product = fun.read_file("product.txt")
                for p in product:
                    print (p.title())
            elif choose_your_op2==2:
                fun.add_item()
            elif choose_your_op2==3:
                fun.update_item()
            elif choose_your_op2==4:
                fun.delete_item()
            else:
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print product menu \n2 - Create a new product \n3 - Update an existing product \n4 - Delete a product\n")
    elif choose_your_op1 ==2:
        while True:
            choose_your_op3 = int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print courier option \n2 - Create new courier \n3 - Update an existing courier \n4 - Delete a courier\n"))
            if choose_your_op3 == 0:
                break
            elif choose_your_op3 == 1:
                couirer = fun.read_file("courier.txt")
                for c in couirer:
                    print (c.title())
            elif choose_your_op3 ==2:
                fun.add_courier()
            elif choose_your_op3 ==3:
                fun.update_courier()
            elif choose_your_op3 ==4:
                fun.delete_courier()
            else:
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print courier option \n2 - Create new courier \n3 - Update an existing courier \n4 - Delete a courier\n")
    elif choose_your_op1 ==3:
        while True:
            choose_your_op4 = int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print order directory \n2 - Create new order \n3 - Update existing order status \n4 - update existing order\n5 - Delete an order\n"))
            if choose_your_op4 == 0:
                break
            elif choose_your_op4 == 1:
                print(orderlist)
            elif choose_your_op4 ==2:
                order_id += 1
                cus_name = input("Please input customer's name\n")
                cus_add = input("Please input customer's address\n")
                cus_phone = input("Please input customer's phone number\n")
                product = fun.read_file("product.txt")
                for p in product:
                    print (product.index(p),p.title())
                cus_product = int(input("Please choose a product by index\n"))
                courier = fun.read_file("courier.txt")
                for c in courier:
                    print (courier.index(c), c.title())
                cus_courier = int(input("Please choose a courier by index\n"))
                cus_status = input("Please input customer's status, <preparing>, <out for delivery>, <finished>\n")
                x = str(order_id)
                x =Orders (order_id, cus_name,cus_add,cus_phone,cus_product,cus_courier,cus_status)
                orderlist.append(x.__dict__)
                statuslist [x.order_id] = {"cus_id": str(order_id), "cus_status":cus_status}
            elif choose_your_op4 ==3:
                print (statuslist)
                cus_id_to_update = input("Please input the customer id you want to update status\n")
                print(orderlist[int(cus_id_to_update)-1])
                # y = str(cus_id_to_update)
                # y.status_check()
                #why can't i call the object method?
                new_status = input("Please input customer's status, <preparing>, <out for delivery>, <finished>\n")
                y.status_change(new_status)
                #why can't i call the object method?
                orderlist[cus_id_to_update-1[cus_status]]=new_status
            elif choose_your_op4 ==4:
                for x in orderlist:
                    print(orderlist.index(x), x)
                    update_order = input("Please input the customer id you want to update\n")
                    item_to_update = input("Please input the customer id you want to update\n")
                    #question: how to update order?
            elif choose_your_op4 ==5:
                for x in orderlist:
                    print(orderlist.index(x), x)
                order_to_delete = input("Please choose the order to delete by order id\n")
                confirmation = input (f"Please confirm you want to delete order {order_to_delete}. y/n").lower()
                if confirmation == "y":
                    del orderlist[int(order_to_delete)-1]
                    del statuslist[int(order_to_delete)]
                    #why is it not working?
            else:
                print ("Please choose the service \n0 - Return to main menu \n1 - Print order directory \n2 - Create new order \n3 - Update existing order status \n4 - update existing order - \n5 - Delete an order\n")    
    else:
        print ("Wrong input. Please input the right option. \nPlease choose the service \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n3 - Order menu")

