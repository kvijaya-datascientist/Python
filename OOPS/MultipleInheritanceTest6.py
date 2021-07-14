class Employee:

    def __init__(self,fn,ln,pay):
      self.firstName = fn
      self.lastName = ln
      self.salary = pay
      self.fullName = fn + ' ' + ln

    @classmethod
    def raisePay(cls,pay):
        return (pay * cls.hike)

class Developer(Employee):
        hike = 1.04

        def __init__(self,fn,ln,pay,skill):
            self.skill = skill
            super().__init__(fn,ln,pay)  # (OR) Employee.__init__(self,fn,ln,pay)

class Manager(Employee):

       def __init__(self,fn,ln,pay,employees=None):
           Employee.__init__(self,fn,ln,pay)
           if employees == None:
               self.dr = []
           else:
               self.dr = employees

       def add_DR(self,emp):
           if emp not in self.dr:
             self.dr.append(emp)

       def remove_DR(self,emp):
            if emp in self.dr:
                self.dr.remove(emp)

       def dr_details(self):
           for emp in self.dr:
            print('DRs--->',emp.fullName)

if __name__ == "__main__":
    dev1 = Developer('hemaja', 'kaja',30000, 'DS')
    dev2 = Developer('gopi', 'chand',30000, 'ML')
    manager1 = Manager('santosh','kumar',90000,[dev1])
    #print(manager1.__dict__)
    print(manager1.dr_details())
    manager1.add_DR(dev2)
    #print(manager1.__dict__)
    print(manager1.dr_details())

