import csv
from DB_Manager import DB_Manager
from inventory import inventory
from person import person
from product import product

# TO TRY THE PRODUCT          
DB_Manager1 = DB_Manager()

def invoice(id, quantity):
      print("Quantity modified. Purchase successful!")
      print("Invoice:")
      print("Item ID", DB_Manager1.get_product_by_id(id).get_id())
      print("Item Name:", DB_Manager1.get_product_by_id(id).get_name())
      print("Quantity demanded (available):", DB_Manager1.get_product_by_id(id).get_quantity())
      print("Price per unit:", DB_Manager1.get_product_by_id(id).get_price())
      print("Total Price: ", DB_Manager1.get_product_by_id(id).get_price() * quantity)
      print("Thank you for your purchase!")
      # check if the following is right
      DB_Manager1.get_product_by_id(id).set_quantity(DB_Manager1.get_product_by_id(id).get_quantity() - quantity)
      DB_Manager1.save_products_to_csv("product.csv")

def customer_options():
    print('''Customer Options:
  1. List available items
  2. Search for item
  3. Buy item
  Choose option (1/2/3):''')
    my_opt = input()
    if my_opt == "1":
      print("Available items:")
      [print(i) for i in DB_Manager1.get_all_products() if i.get_quantity() > 0] 
    return my_opt

def create_product():
  id = int(input("Enter item ID: "))
  while DB_Manager1.get_product_by_id(id) is not None:
    try :
      raise ValueError(f"Product with id {id} already exists")
    except ValueError as e:            
      print(e)
    id = int(input("Enter another item ID: "))

  name = input("Enter item name: ")
  quantity = int(input("Enter quantity: "))
  price = float(input("Enter price: "))
  category = input("Enter category: ")
  DB_Manager1.create_product(id, name, quantity, price, category)
  print("Item added successfully!")
  DB_Manager1.save_products_to_csv("product.csv")

def create_person():
  id = int(input("Enter person ID: "))
  while DB_Manager1.get_person_by_id(id) is not None:
    try :
      raise ValueError(f"Person with id {id} already exists")
    except ValueError as e:            
      print(e)
    id = int(input("Enter another person ID: "))
  name = input("Enter person name: ")
  type = input("Enter person type (Customer/Supplier): ")
  location = input("Enter person location: ")
  phone_number = input("Enter person phone number: ")
  email = input("Enter person email: ")
  age = int(input("Enter person age: "))
  gender = input("Enter person gender: ")
  DB_Manager1.create_person(id, name, type, location, phone_number, email, age, gender)
  print("Person added successfully!")
  DB_Manager1.save_persons_to_csv("person.csv")

def create_inventory():
  id = int(input("Enter inventory ID: "))
  while DB_Manager1.get_inventory_by_id(id) is not None:
    try :
      raise ValueError(f"Inventory with id {id} already exists")
    except ValueError as e:            
      print(e)
    id = int(input("Enter another inventory ID: "))
  name = input("Enter inventory name: ")
  capacity = int(input("Enter inventory capacity: "))
  location = input("Enter inventory location: ")
  expenses = float(input("Enter inventory expenses: "))
  DB_Manager1.create_inventory(id, name, capacity, location, expenses)
  print("Inventory added successfully!")
  DB_Manager1.save_inventories_to_csv("inventory.csv")

def update_product():
  id1 = int(input("Enter item ID: "))
  new = DB_Manager1.get_product_by_id(id1)
  
  if new is None:
    try :
      raise ValueError(f"Product with id {id1} does not exist")
    except ValueError as e:            
      print(e)
    print("Product not found")
    exit()
  else:
    my_option = input("what would you like to update? (enter the number) --> 1: name, 2: quantity, 3: price, 4: category")
    if my_option not in ["1", "2", "3", "4"]:
      print("Invalid option. Please try again.")
      exit()
    if my_option == "1":
      new.set_name(input("Enter new name: "))

    if my_option == "2":
      new.set_quantity(input("Enter new quantity: "))

    if my_option == "3":
      new.set_price(input("Enter new price: "))

    if my_option == "4":
      new.set_category(input("Enter new category: "))

    DB_Manager1.update_product(id1, new)
    DB_Manager1.save_products_to_csv("product.csv")
    return id1, new 

def update_person():
  id1 = int(input("Enter person ID: "))
  new = DB_Manager1.get_person_by_id(id1)
  if new is None:
    try :
      raise ValueError(f"Person with id {id1} does not exist")
    except ValueError as e:            
      print(e)
    print("Person not found")
    exit()
  else:
    my_option = input("what would you like to update? (enter the number) --> 1: name, 2: type, 3: location, 4: phone number, 5: email, 6: age, 7: gender ")
    if my_option not in ["1", "2", "3", "4", "5", "6", "7"]:
      print("Invalid option. Please try again.")
      exit()
    if my_option == "1":
      new.set_name(input("Enter new name: "))

    if my_option == "2":
      new.set_type(input("Enter new type: "))

    if my_option == "3": 
      new.set_location(input("Enter new location: "))

    if my_option == "4":
      new.set_phone_number(input("Enter new phone number: "))

    if my_option == "5":
      new.set_email(input("Enter new email: "))

    if my_option == "6":
      new.set_age(input("Enter new age: "))

    if my_option == "7":
      new.set_gender(input("Enter new gender: "))

  DB_Manager1.update_person(id1, new)
  DB_Manager1.save_persons_to_csv("person.csv")
  return id1, new

def update_inventory():
  id1 = int(input("Enter inventory ID: "))
  new = DB_Manager1.get_inventory_by_id(id1)
  if new is None:
    try : 
      raise ValueError(f"Inventory with id {id1} does not exist")
    except ValueError as e:            
      print(e)
    print("Inventory not found")
    exit()
  else:
    my_option = input("what would you like to update? (enter the number) --> 1: name, 2: capacity, 3: location, 4: expenses ")
    if my_option not in ["1", "2", "3", "4"]:
      print("Invalid option. Please try again.")
      exit()
    if my_option == "1":
      new.set_name(input("Enter new name: "))

    if my_option == "2":
      new.set_capacity(input("Enter new capacity: "))

    if my_option == "3":
      new.set_location(input("Enter new location: "))

    if my_option == "4":
      new.set_expenses(input("Enter new expenses: "))
   
    DB_Manager1.update_inventory(id1, new)
    DB_Manager1.save_inventories_to_csv("inventory.csv")
    return id1, new
  
def delete_inventory():
  id1 = int(input("Enter inventory ID: "))
  while DB_Manager1.get_inventory_by_id(id1) is None:
    try :
      raise ValueError(f"Can't delete inventory with id {id1} because it does not exist")
    except ValueError as e:            
      print(e)
    id1 = int(input("Enter another inventory ID to delete: "))
  DB_Manager1.delete_inventory(id1)
  DB_Manager1.save_inventories_to_csv("inventory.csv")
  print("Inventory deleted successfully!")

def delete_person():
  id1 = int(input("Enter person ID: "))
  while DB_Manager1.get_person_by_id(id1) is None:
    try :
      raise ValueError(f"Can't delete person with id {id1} because it does not exist")
    except ValueError as e:            
      print(e)
    id1 = int(input("Enter another person ID to delete: "))
  DB_Manager1.delete_person(id1)
  DB_Manager1.save_persons_to_csv("person.csv")
  print("Person deleted successfully!")

def delete_product():
  id1 = int(input("Enter item ID: "))
  while DB_Manager1.get_product_by_id(id1) is None:
    try :
      raise ValueError(f"Can't delete product with id {id1} because it does not exist")
    except ValueError as e:            
      print(e)
    id1 = int(input("Enter another item ID to delete: "))
  DB_Manager1.delete_product(id1)
  DB_Manager1.save_products_to_csv("product.csv")
  print("Item deleted successfully!")


try:
    DB_Manager1.load_inventories_from_csv("inventory.csv")
except FileNotFoundError:
    pass

try:
    DB_Manager1.load_persons_from_csv("person.csv")
except FileNotFoundError:
    pass

try:
    DB_Manager1.load_products_from_csv("product.csv")
except FileNotFoundError:
    pass



def main():
  # ROLE = ADMIN OR CUSTOMER
  role = input("Select your role (Admin / Customer): ")
  if role not in ["Admin", "Customer"]:
    print("Invalid role. Please try again.")
    exit()
  #ROLE = ADMIN
  while True:
    if role == "Admin":
      print('''Admin Options: would you like to modify -->
    1. Products
    2. Persons
    3. Inventories
    Choose option (1/2/3):''')
      my_option = input()
      if my_option not in ["1", "2", "3"]:
        print("Invalid option. Please try again.")
        continue
      print('''Product Options:
    1. Add new item
    2. Edit existing item
    3. Delete item
    4. List all items
    5. Search for item
    6. Terminate program
    Choose option (1/2/3/4/5/6): ''')
      my_option2 = input()
      if my_option2 not in ["1", "2", "3", "4", "5", "6"]:
        print("Invalid option. Please try again.")
        continue

      if my_option == "1":
        if my_option2 == "1":
          create_product()


        if my_option2 == "2":
          id1, new = update_product()
          print("Updated Product:", DB_Manager1.get_product_by_id(id1))

        if my_option2 == "3":
          delete_product()


        if my_option2 == "4":
          print("Available items:")
          print("ID | Name | Quantity | Price | Category")
          for p in DB_Manager1.get_all_products():
            print(p)


        if my_option2 == "5":
          print("Enter item name: ")
          name = input()
          for p in DB_Manager1.search_products_by_name(name):
            print(p)
          

        if my_option2 == "6":
          print("Terminating program. Goodbye!")
          exit()


      if my_option == "2":
        if my_option2 == "1":
            create_person()


        if my_option2 == "2":
          id1, new = update_person()
          print("Updated Person:", DB_Manager1.get_person_by_id(id1))



        if my_option2 == "3":
          delete_person()

        
        if my_option2 == "4":
          print("Available persons:")
          print("ID | Name | Type | Location | Phone Number | Email | Age | Gender")
          for person in DB_Manager1.get_all_persons():
            print(person)

        
        if my_option2 == "5":
          print("Enter person name: ")
          name = input()
          for p in DB_Manager1.search_persons_by_name(name):
            print(p)



        if my_option2 == "6":
          print("Terminating program. Goodbye!")
          exit()


      if my_option == "3":
        if my_option2 == "1":
            create_inventory()
        


        if my_option2 == "2":
          id1, new = update_inventory()
          print("Updated Inventory:", DB_Manager1.get_inventory_by_id(id1)) 


        if my_option2 == "3":
          delete_inventory()


        if my_option2 == "4":
          print("Available inventories:")
          #print the headers of the inventory table
          print("ID | Name | Capacity | Location | Expenses")
          for inventory in DB_Manager1.get_all_inventories():
            print(inventory)


        if my_option2 == "5":
          print("Enter inventory name: ")
          name = input()
          for p in DB_Manager1.search_inventories_by_name(name):
            print(p)
          


        if my_option2 == "6":
          print("Terminating program. Goodbye!")
          exit()



        
    # ROLE = CUSTOMER

    if role == "Customer":
      my_opt = customer_options()




      if my_opt == "2":
        print("Enter item name: ")
        name = input()
        search_product = DB_Manager1.search_products_by_name(name)
        for p in search_product:
          if p.get_quantity() > 0:
            print("ID | Name | Quantity | Price | Category")
            print(p)

          if p.get_quantity() == 0:
            print(f"{p.get_name()} is currently out of stock")
    


      if my_opt == "3":
        print("Enter item ID to buy: ")
        id = int(input())
        used_product = DB_Manager1.get_product_by_id(id)
        print(DB_Manager1.get_product_by_id(id))
        while DB_Manager1.get_product_by_id(id) is None:
          try :
            raise ValueError(f"Product with id {id} does not exist")
          except ValueError as e:            print(e) 
          print("Product not found")
          id = int(input("Enter another item ID to buy: "))
        print("Enter quantity: ")
        quantity = int(input())
    # check if te following is right ?
        if quantity > DB_Manager1.get_product_by_id(id).get_quantity():
          print(f"Only {DB_Manager1.get_product_by_id(id).get_quantity()} is available")
          print(f"Would you like to buy {DB_Manager1.get_product_by_id(id).get_quantity()} instead? (yes/no)")
          answer = input()
          
          if answer == "yes":
            quantity = DB_Manager1.get_product_by_id(id).get_quantity()       
            invoice(id, quantity)

          if answer == "no":
            print("No problem. Quantity unavailable. Please try again")

        else:
          invoice(id, quantity)


if __name__ == "__main__":
  main()


      