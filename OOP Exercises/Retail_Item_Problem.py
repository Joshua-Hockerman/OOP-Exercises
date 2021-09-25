import Retail_item as rt

item1 = rt.Retailitem("Jacket", 12, "$59.95")
item2 = rt.Retailitem("Designer Jeans", 40, "$34.95")
item3 = rt.Retailitem("Shirt", 20, "$24.95")

print(
    "The first item is a "
    + item1.get_description()
    + ", we have "
    + str(item1.get_units())
    + " of them in stock, and they cost "
    + item1.get_price()
)
print(
    "The first item is "
    + item2.get_description()
    + ", we have "
    + str(item2.get_units())
    + " of them in stock, and they cost "
    + item2.get_price()
)
print(
    "The first item is a "
    + item3.get_description()
    + ", we have "
    + str(item3.get_units())
    + " of them in stock, and they cost "
    + item3.get_price()
)
