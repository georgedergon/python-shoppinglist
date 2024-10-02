shoppinglist =[]
#reate a shoppinglist shopinglist.py
#we ask the user "please insert the article you want to add to your shoppinglist")
def add_item():
   item = input("Please {insert} the article you want to add to your shoppinglist: ")
   print(f"You want to buy [Item]")
   shoppinglist.append(item)    


#check the shopping list is empty
def check_shoppinglist():
   if not shoppinglist:
      print(f" your shoppinglist is empty")
   else:
      print(f" your shoppinglist")
   for item in shoppinglist:
      print (item)


add_item()
check_shoppinglist()