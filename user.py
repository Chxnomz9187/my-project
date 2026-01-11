class Person:
    def __init__(self, name, email, phone):
        self.__name = name
        self.__email = email
        self.__phone = phone


class Admin(Person):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
