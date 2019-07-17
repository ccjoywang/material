import datetime


class Person:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def speak(self):
        print('hello')

    def walk(self):
        print('walking away')

    def cry(self):
        print("I'm crying!!!")

    def get_name(self):
        return self.name

    def get_age(self):
        today = datetime.date.today()
        age = today.year - self.birthday.year
        return age


# usage
mary = Person('Mary', datetime.date(2000, 1, 1))
mary.speak()
mary.walk()
mary.cry()
print(mary.get_name())
print(mary.get_age())
