class Employee:

    def __init__(self,fn,ln,pay):
      self.firstName = fn
      self.lastName = ln
      self.salary = pay

    @classmethod
    def raisePay(cls,pay):
        return (pay * cls.hike)

class Developer(Employee):
        hike = 1.04

        def __init__(self,fn,ln,pay,skill):
            self.skill = skill
            super().__init__(fn,ln,pay)  # (OR) Employee.__init__(self,fn,ln,pay)

if __name__ == "__main__":
    dev1 = Developer('hemaja', 'kaja',30000, 'DS')

    print(f'{dev1.firstName} details-->',dev1.__dict__)
    print(f' {dev1.firstName} salary after hike =',dev1.raisePay(dev1.salary)) # Inheriting the employee class Varibles & Methods
    print(f'{dev1.firstName} skill set is',dev1.skill)
