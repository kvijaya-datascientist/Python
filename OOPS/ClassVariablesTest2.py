"""
Class variables : are variables that are shared among all instances of a class
Instance variables : are variables that are unique to each instance of a class
"""
class Employee:
    raise_amount = 1.04
    no_of_emps =0
    def __init__(self,fn,ln,pay):
        self.firstName = fn
        self.lastName = ln
        self.pay = pay
        self.email = fn + '.' + ln + '@gmail.com'

        Employee.no_of_emps += 1
if __name__ == "__main__":
    print(Employee.no_of_emps)  # prints no.os instances of Employee class
    emp1 = Employee('vijaya', 'lakshmi', 30000)
    emp2 = Employee('satya','srikanth', 40000)

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(emp1.__dict__)  # here we can't see 'raise_amount' value
print(Employee.__dict__)  # here we can see/access 'raise_amount' value , since it is class variable

Employee.raise_amount = 1.05 # overriding raise_amount value

print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

emp1.raise_amount = 2.3

print(emp1.__dict__) # we can see 'raise_amount' bcoz in above line we are setting the value
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

print(Employee.no_of_emps)



