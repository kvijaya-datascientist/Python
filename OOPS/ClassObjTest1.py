
class Employee:
    def __init__(self,fn,ln,sal):
        self.firstName = fn
        self.lastName = ln
        self.pay = sal
        self.email =  fn + '.' + ln + '@gmail.com'

    def fullName(self):
        return '{} {}'.format(self.firstName,self.lastName)

if __name__ == "__main__":
    emp1 = Employee('vijaya','kaja',60000)
    emp2 = Employee('satya' , 'srikanth' , 70000)

print(emp1.email)
print(emp2.lastName)

print(emp1.fullName())
print(Employee.fullName(emp1))


