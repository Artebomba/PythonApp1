"""
from Calculator import add
print(add(4,2))
"""
class Employee:
    totalEmployees = 0 
    def __init__(self, empName, age, designation, salary):
        self.empName = str(empName)
        self.age = int(age)
        self.designation = str(designation)
        self.salary = float(salary)
        Employee.totalEmployees += 1
    def getEmpDetailes(self):
        return self.empName, self.age, self.designation, self.salary
    def updateSalary(self, newSalary):
        self.salary = float(newSalary)
        print("Successfuly updated!")
        return self.salary
    
class Intern(Employee):
    def __init__(self, empName, age, designation, salary, internPeriod):
        self.internPeriod = int(internPeriod)
        Employee.__init__(self, empName, age, designation, salary)
    
    def getPeriod(self):
        print("Intership period is ", self.internPeriod)
        
emp1 = Employee("John", 45, "taxist", 3250.23 )
emp2 = Employee("Sean", 32, "dentist", 5543.5 )
int1 = Intern("Artem", 27, "DevOps", 3560.0, 3)


"""
print(Employee.totalEmployees)
print(emp1.getEmpDetailes())
emp1.updateSalary(3456.6)
print(emp1.getEmpDetailes())
"""
print(int1.getEmpDetailes())
print(int1.getPeriod())

