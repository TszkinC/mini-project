import func_for_mini5 as fun

# we are no longer reading products, couriers, orders and order statuses from files
# we are now reading data from database tables
# CREATE order status list

status_list={1:"preparing", 2:"out for delivery",3:"done"}

print ("Welcome to Cafe Python. What can I do for you?\n")
    
while True:
    choose_your_op1=int(input ("\nPlease choose the service below \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n3 - Order menu\n"))
    if choose_your_op1==0:
        print ("Thanks for coming!")
        break
    elif choose_your_op1==1:
        while True:
            choose_your_op2=int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print menu option \n2 - Create a new product \n3 - Update an existing product \n4 - Delete a product\n"))
            if choose_your_op2==0:
                break
            elif choose_your_op2==1:
                fun.print_table('product')
            elif choose_your_op2==2:    
                fun.add_product()
            elif choose_your_op2==3:
                fun.update_product()
            elif choose_your_op2==4:
                fun.delete_product()
            else:
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print product menu \n2 - Create a new product \n3 - Update an existing product \n4 - Delete a product\n")
    elif choose_your_op1==2:
        while True:
            choose_your_op3=int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print courier option \n2 - Create new courier \n3 - Update an existing courier \n4 - Delete a courier\n"))
            if choose_your_op3==0:
                break
            elif choose_your_op3==1:
                fun.print_table('courier')
            elif choose_your_op3==2:
                fun.add_courier()
            elif choose_your_op3==3:
                fun.update_courier()
            elif choose_your_op3==4:
                fun.delete_courier()
            else:
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print courier option \n2 - Create new courier \n3 - Update an existing courier \n4 - Delete a courier\n")
    elif choose_your_op1==3:
        while True:
            choose_your_op4=int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print order directory \n2 - Create new order \n3 - Update existing order status \n4 - update existing order\n5 - Delete an order\n"))
            if choose_your_op4==0:
                break
            elif choose_your_op4==1:
                fun.print_table('orders')
            elif choose_your_op4==2:
                fun.add_new_order()
            elif choose_your_op4==3:
                fun.update_order_status()
            elif choose_your_op4==4:
                fun.update_order_detail()
            elif choose_your_op4==5:
                fun.delete_order()
            else:
                print ("Please choose the service \n0 - Return to main menu \n1 - Print order directory \n2 - Create new order \n3 - Update existing order status \n4 - update existing order - \n5 - Delete an order\n")    
    else:
        print ("Wrong input. Please input the right option. \nPlease choose the service \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n3 - Order menu")