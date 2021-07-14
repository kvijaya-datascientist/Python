"""
Instance method : When creating an instance method, the first parameter is always self. You can name it anything you want,
but the meaning will always be the same, and you should use self since it's the naming convention.
self is (usually) passed hiddenly when calling an instance method; it represents the instance calling the method.

Class method : The idea of class method is very similar to instance method, only difference being that instead of passing
the instance hiddenly as a first parameter, we're now passing the class itself as a first parameter.

Static method : This type of method takes neither a self nor a cls parameter.Therefore a static method can neither modify object state nor class state.

Instance Methods: The most common method type. Able to access data and properties unique to each instance.
Static Methods: Cannot access anything else in the class. Totally self-contained code.
Class Methods: Can access limited methods in the class. Can modify class specific details.

decorator pattern(decorator) :  Decorators are simply functions.Like any function, decorators perform a task.
The difference here is that decorators apply logic or change the behavior of other functions.
They are an excellent way to reuse code, and can help to separate logic into individual concerns.

NOTE - The decorator pattern is Python's preferred way of defining static or class methods
"""
class Employee:
    raise_amount = 1.04
    def __init__(self,fn,ln,pay):
        self.firstName = fn
        self.lastName = ln
        self.pay = pay
        self.email = fn + '.' + ln + '@gmail.com'

    def fullName(self):     # Instance method
        return '{} {}'.format(self.firstName,self.lastName)

    @classmethod
    def check_raise_amount(cls,amount):     # Class method
            cls.raise_amount = amount
    @classmethod
    def createInstanceFromString(cls,empString):
        firstName,lastName,pay = empString.split('-')
        return cls(firstName,lastName,pay)

    @staticmethod
    def is_weekday(day):     # Static method
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

if __name__ == "__main__":
 emp1 = Employee('hemaja','kaja',80000)
 emp2 = Employee('gopi', 'chandu', 40000)

 print(Employee.raise_amount)
 print(emp1.raise_amount)
 print(emp2.raise_amount)

 emp1.check_raise_amount(1000)

 print(Employee.raise_amount)
 print(emp1.raise_amount)
 print(emp2.raise_amount)

"""
Creating the instance from employee string,below is example
"""
emp1_string = 'vijaya-lakshmi-30000'
emp2_string = 'rahul-chidri-40000'
emp3_string = 'maanvi-chidri-70000'

new_emp1 = Employee.createInstanceFromString(emp1_string)

print(new_emp1.firstName)
print(new_emp1.email)

"""
Finding given day is weekday or holiday
"""
import datetime

given_day = datetime.date(2021,7,11)

print(Employee.is_weekday(given_day))
