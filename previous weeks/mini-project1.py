# # add some product names
# CREATE products list
print ("Welcome to Cafe Python. What can I do for you?\n")
product = ["pasta", "quiche", "sandwich", "panini","coffee", "tea", "coke_zero", "juice"]
    
# PRINT main menu options
main_menu = {0: "Exit APP", 1: "Print menu option"}
second_menu = {0: "Return to main menu", 1: "Print menu option",2: "Create new product", 3:"Update existing product", 4:"Delete product"}

def print_menu1():
    for key in main_menu.keys():
        print (key, "--", main_menu[key])
        
def print_menu2():
    for key in second_menu.keys():
        print (key, "--", second_menu[key])
        
def add_item ():
    global product
    x = input ("What would you like to add?")
    new_product = product.append(x)
    product = new_product
    print (product)
    
def update_item():
    y = input ("what would you like to change?")
    
def delete_item():
    z = input ("Which item would you like to delete?")
    
while True:
    #print_menu1()
    choose_your_op1 = int(input ("\nPlease choose the service \n0 - Exit APP \n1 - Select product from menu\n"))
    if choose_your_op1 ==0:
        print ("Thanks for visiting us!")
        break
    elif choose_your_op1 ==1:
        print (input("What would you like to order from the menu?\n"))
        while True:
            #print_menu2()
            choose_your_op2 = int(input ("\nPlease choose the service \n0 - Return to main menu \n1 - Print menu option \n2 - Create new product \n3 - Update existing product \n4 - Delete product\n"))
            print (choose_your_op2)
            if choose_your_op2 == 0:
                break
            elif choose_your_op2 == 1:
                print (product)
            elif choose_your_op2 == 2:
                add_item
            elif choose_your_op2 ==3:
                update_item
                # for product in product_list:
                #print (product, product_list.index)
            elif choose_your_op2 ==4:
                delete_item
            else:
                print ("Wrong input. Please input the right option. \n0 - Return to main menu \n1 - Print menu option \n2 - Create new product \n3 - Update existing product \n4 - Delete product")
        break
    else:
        print ("Wrong input. Please input the right option. \n0 - Exit APP \n1 - Print menu option")

# 0 - Exit APP
# 1 - Print menu option
# 2 - Create new product
# 3 - Update existing product
# 4 - Delete product
# GET user input for main menu option
# IF user input is 0:
# EXIT app
    
# # products menu
# ELSE IF user input is 1:
# PRINT product menu options
# GET user input for product menu option
# IF user input is 0:
# RETURN to main menu
# ELSE IF user input is 1:
# PRINT products list
# ELSE IF user input is 2:
# # CREATE new product
# GET user input for product name
# APPEND product name to products list
# ELSE IF user input is 3:
# # STRETCH GOAL - UPDATE existing product
# PRINT product names with its index value
# GET user input for product index value
# GET user input for new product name
# UPDATE product name at index in products list
# ELSE IF user input is 4:
# # STRETCH GOAL - DELETE product
# PRINT products list
# GET user input for product index value
# DELETE product at index in products list