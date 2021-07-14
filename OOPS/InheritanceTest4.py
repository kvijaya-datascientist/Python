class Employee:
    hike = 1.04
    def __init__(self,fn,ln,pay):
      self.firstName = fn
      self.lastName = ln
      self.salary = pay

    @classmethod
    def raisePay(cls,pay):
        return (pay * cls.hike)

class Developer(Employee):
        pass


if __name__ == "__main__":
    emp1 = Developer('hemaja', 'kaja',30000)

    print(emp1.__dict__)
    print(f' {emp1.firstName} salary after hike =',emp1.raisePay(emp1.salary)) # Inheriting the employee class Varibles & Methods