class person:
    def __init__(self, id, name, type, location, phone_number, email, age, gender):
       self.__id = id
       self.__name = name
       self.__type = type
       self.__location = location
       self.__phone_number = phone_number
       self.__email = email
       self.__age = age
       self.__gender = gender

    def __str__(self):
            return f"({self.__id}, {self.__name}, {self.__type}, {self.__location}, {self.__phone_number}, {self.__email}, {self.__age}, {self.__gender})"


    def get_id(self):
       return(self.__id)

    def get_name(self):
       return(self.__name)

    def get_type(self):
       return(self.__type)

    def get_location(self):
       return(self.__location)

    def get_phone_number(self):
       return(self.__phone_number)

    def get_email(self):
       return(self.__email)

    def get_age(self):
       return(self.__age)

    def get_gender(self):
       return(self.__gender)

    def set_id(self, id):
       self.__id = id

    def set_name(self, name):
       self.__name = name

    def set_type(self, type):
       self.__type = type

    def set_location(self, location):
       self.__location = location

    def set_phone_number(self, phone_number):
       self.__phone_number = phone_number

    def set_email(self, email):
       self.__email = email

    def set_age(self, age):
       self.__age = age

    def set_gender(self, gender):
       self.__gender = gender