import csv
from inventory import inventory
from person import person
from product import product




#--------------------------------------------------------------------


class DB_Manager:
  def __init__(self):
      
      self.__persons = []
      self.__products = []
      self.__inventories = []


#products to load
  def load_products_from_csv(self, filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            product1 = product(
                int(row['id']),
                row['name'],
                int(row['quantity']),
                float(row['price']),
                row['category'],
#                row['dimensions'],
#                row['storing_conditions']
            )

            self._DB_Manager__products.append(product1)


  def save_products_to_csv(self, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([
            "id", "name", "quantity", "price",
            "category"#, "dimensions", "storing_conditions"
        ])

        # Write data
        for p in self._DB_Manager__products:
            writer.writerow([
                p.get_id(),
                p.get_name(),
                p.get_quantity(),
                p.get_price(),
                p.get_category(),
#                p.get_dimensions(),
#                p.get_storing_conditions()
            ])

            
    
# persons to load
  def load_persons_from_csv(self, filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            person1 = person(
                int(row['id']),
                row['name'],
                row['type'],
                row['location'],
                row['phone_number'],
                row['email'],
                row['age'],
                row['gender'])
          

            self._DB_Manager__persons.append(person1)


  def save_persons_to_csv(self, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([
            "id", "name", "type", "location",
            "phone_number", "email", "age", "gender"
        ])

        # Write data
        for p in self._DB_Manager__persons:
            writer.writerow([
                p.get_id(),
                p.get_name(),
                p.get_type(),
                p.get_location(),
                p.get_phone_number(),
                p.get_email(),
                p.get_age(),
                p.get_gender()
            ])


# inventories to load    
  def load_inventories_from_csv(self, filename):
    with open(filename, mode='r') as file:
        reader = csv.DictReader(file)

        for row in reader:
            inventory1 = inventory(
                int(row['id']),
                row['name'],
                row['capacity'],
                row['location'],
                row['expenses']
                
            )

            self._DB_Manager__inventories.append(inventory1)


  def save_inventories_to_csv(self, filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write header
        writer.writerow([
            "id", "name", "capacity", "location",
            "expenses"
        ])

        # Write data
        for p in self._DB_Manager__inventories:
            writer.writerow([
                p.get_id(),
                p.get_name(),
                p.get_capacity(),
                p.get_location(),
                p.get_expenses()
            ])

#------

  # create 
  
  def create_person(self, id, name, type, location, phone_number, email, age, gender):
      if self.get_person_by_id(id) is not None:
        raise ValueError(f"Person with id {id} already exists")
      person1 = person(id, name, type, location, phone_number, email, age, gender)
      self.__persons.append(person1)
      return person1

  def create_product(self, id, name, quantity, price, category):
      if self.get_product_by_id(id) is not None:
        raise ValueError(f"Product with id {id} already exists")
      product1 = product(id, name, quantity, price, category)
      self.__products.append(product1)
      return product1

  def create_inventory(self, id, name, capacity, location, expenses):
      if self.get_inventory_by_id(id) is not None:
        raise ValueError(f"Inventory with id {id} already exists")  
      inventory1 = inventory(id, name, capacity, location, expenses)
      self.__inventories.append(inventory1)
      return inventory1


#--------

  
  #read

  def get_all_persons(self): return self.__persons
  def get_all_products(self): return self.__products
  def get_all_inventories(self): return self.__inventories

#--

  def get_person_by_id(self, id):
      for p in self.__persons:
          if p.get_id() == id: return p
      return None

  def search_persons_by_name(self, name):
    names_person = []
    for p in self.__persons:
       if name.lower() in p.get_name().lower():  
        names_person.append(p)
    return names_person

#--
  

  def get_product_by_id(self, id):
      for prod in self.__products:
          if prod.get_id() == id: return prod
      return None

  def search_products_by_name(self, name):
    names_product = []
    for prod in self.__products:
        if name.lower() in prod.get_name().lower():
          names_product.append(prod)
    return names_product

#--

  def get_inventory_by_id(self, id):
      for inv in self.__inventories:
          if inv.get_id() == id: return inv
      return None

  def search_inventories_by_name(self, name):
    names_inventory = []
    for inv in self.__inventories:
      if name.lower() in inv.get_name().lower():
        names_inventory.append(inv)
    return names_inventory


#------

  #update
  def update_person(self, id, new_person):
      old_person = self.get_person_by_id(id)
      old_person = new_person
      return new_person
      
# def update_person(self, id, new_person):
#     for i, p in enumerate(self.__persons):
#         if p.get_id() == id:
#             self.__persons[i] = new_person
#             return new_person
#     return None

  def update_product(self, id, new_product):
      old_product = self.get_product_by_id(id)
      old_product = new_product
      return new_product
  
  # def update_product(self, id, new_product):
  #   for i, p in enumerate(self.__products):
  #       if p.get_id() == id:
  #           self.__products[i] = new_product
  #           return new_product
  #   return None
    

  def update_inventory(self, id, new_inventory):
      old_inventory = self.get_inventory_by_id(id)
      old_inventory = new_inventory
      return new_inventory
  
  # def update_inventory(self, id, new_inventory):
  #   for i, p in enumerate(self.__inventories):
  #       if p.get_id() == id:
  #           self.__inventories[i] = new_inventory
  #           return new_inventory
  #   return None

#------------
  
#delete
  def delete_person(self, id):
     old_person = self.get_person_by_id(id)
     self.__persons.remove(old_person)
       
      

  def delete_product(self, id):
     old_product = self.get_product_by_id(id)
     self.__products.remove(old_product)


  def delete_inventory(self, id):
    old_inventory = self.get_inventory_by_id(id)
    self.__inventories.remove(old_inventory)

#------------
