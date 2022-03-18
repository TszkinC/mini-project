#function to read file
def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
        return [line.strip() for line in lines]

#function to add to file
def add_to_file(filename, item):
    with open(filename, 'a') as f:
        f.write(item.lower()+"\n")

#function to write to file
def write_to_file(filename, items):
    with open(filename, 'w') as f:
        for item in items:
            f.write(item.lower()+'\n')
        
#function to add item to product list
def add_item ():
    """function to add new item to product list"""
    adding_item = str(input ("What would you like to add?\n"))
    productlist = read_file("product.txt")
    if adding_item in productlist:
        print ("Product exists! Please try again!")
    else:
        add_to_file ("product.txt",adding_item)
        read_product = read_file("product.txt")
        for line in read_product:
            print (line.rstrip().title())


#function to update product list
def update_item():
    """function to update product list"""
    read_product = read_file("product.txt")
    for line in read_product:
        print (read_product.index(line),line.title())
    old_item = int(input ("Which item would you like to change?\n"))
    new_item = input ("What do you want to replace it by?")
    read_product [old_item] = new_item
    write_to_file("product.txt", read_product)

#function to delete item from product list
def delete_item():
    """function to delete an item from product list"""
    #print product list
    read_product = read_file("product.txt")
    for line in read_product:
        print (read_product.index(line),line.title())
    old_item = int(input ("Which item would you like to change?\n"))
    read_product.pop(old_item) 
    write_to_file("product.txt", read_product)

#function to add courier
def add_courier ():
    """function to add new item to courier list"""
    adding_item = str(input ("What would you like to add?\n"))
    courierlist = read_file("courier.txt")
    if adding_item in courierlist:
        print ("Courier exists! Please try again!")
    else:
        add_to_file ("courier.txt",adding_item)
        read_courier = read_file("courier.txt")
        for line in read_courier:
            print (line.rstrip().title())


#function to update courier
def update_courier():
    """function to update courier list"""
    read_courier = read_file("courier.txt")
    for line in read_courier:
        print (read_courier.index(line),line.title())
    old_item = int(input ("Which courier would you like to change?\n"))
    new_item = input ("What do you want to replace it by?")
    read_courier [old_item] = new_item
    write_to_file("courier.txt", read_courier)
    
#function to delete courier
def delete_courier():
    """function to delete an item from courier list"""
    #print product list
    read_courier = read_file("courier.txt")
    for line in read_courier:
        print (read_courier.index(line),line.title())
    old_item = int(input ("Which item would you like to change?\n"))
    read_courier.pop(old_item) 
    write_to_file("courier.txt", read_courier)
    
