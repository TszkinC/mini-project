import func_for_mini as fun
#LOAD products list from products.txt
#LOAD couriers list from couriers.txt
def openfile(filename):
    product=[]
    with open (filename,"r") as f:
        read_product = f.readlines()
        for line in read_product:
            product.append(line.rstrip())
    return product
product = openfile("product.txt")
courier = openfile("courier.txt")

print ("Welcome to Cafe Python. What can I do for you?\n")
    
while True:
    choose_your_op1 = int(input ("\nPlease choose the service \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n"))
    if choose_your_op1 ==0:
        product.close()
        courier.close()
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
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print menu option \n2 - Create new product \n3 - Update existing product \n4 - Delete product")    
    else:
        print ("Wrong input. Please input the right option. \nPlease choose the service \n0 - Exit APP \n1 - Product menu\n2 - Courier menu\n")

