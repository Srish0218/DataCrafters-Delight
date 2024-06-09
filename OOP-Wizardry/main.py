class Item:
    #method
    def calculate_price(self , x , y):
        return x * y


# function
def calculate_price(self , x , y):
    return x * y
# instances (object)
item1 = Item()
item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calculate_price(item1.price, item1.quantity))

item2 = Item()
item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item1.calculate_price(item2.price, item2.quantity))


