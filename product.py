class product:
    def __init__(self, id, name, quantity,price,category):
      self.__id = id
      self.__name = name
      self.__quantity = quantity
      self.__price = price
      self.__category = category
#      self.__dimensions = dimensions
#      self.__storing_conditions = storing_conditions


    def __str__(self):
          return f"({self.__id}, {self.__name}, {self.__quantity}, {self.__price}, {self.__category})"


    def get_id(self):
      return(self.__id)

    def get_name(self):
      return(self.__name)

    def get_quantity(self):
      return(self.__quantity)

    def get_price(self):
      return(self.__price)

    def get_category(self):
      return(self.__category)

    # def get_dimensions(self):
    #   return(self.__dimensions)

    # def get_storing_conditions(self):
    #   return(self.__storing_conditions)

    def set_id(self, id):
      self.__id = id

    def set_name(self, name):
      self.__name = name

    def set_quantity(self, quantity):
      self.__quantity = quantity

    def set_price(self, price):
      self.__price = price

    def set_category(self, category):
      self.__category = category

#    def set_dimensions(self, dimensions):
#      self.__dimensions = dimensions

#    def set_storing_conditions(self, storing_conditions):
#      self.__storing_conditions = storing_conditions