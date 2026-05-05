class inventory:
    def __init__(self, id, name, capacity, location, expenses):
       self.__id = id
       self.__name = name
       self.__capacity = capacity
       self.__location = location
       self.__expenses = expenses

    def __str__(self):
           return f"({self.__id}, {self.__name}, {self.__capacity}, {self.__location}, {self.__expenses})"


    def get_id(self):
     return(self.__id)

    def get_name(self):
      return(self.__name)

    def get_capacity(self):
      return(self.__capacity)

    def get_location(self):
      return(self.__location)

    def get_expenses(self):
      return(self.__expenses)

    def set_id(self, id):
      self.__id = id

    def set_name(self, name):
      self.__name = name

    def set_capacity(self, capacity):
      self.__capacity = capacity

    def set_loaction(self, location):
      self.__location = location

    def set_expenses(self, expenses):
      self.__expenses = expenses
