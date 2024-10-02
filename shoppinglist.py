shoppinglist =[]
#reate a shoppinglist shopinglist.py
#we ask the user "please insert the article you want to add to your shoppinglist")
def add_item():
   item = input("Please {insert} the article you want to add to your shoppinglist: ")
   print(f"You want to buy [Item]")
   shoppinglist.append(item)    
   
add_item()

def show_shoppinglist():
   item = input()