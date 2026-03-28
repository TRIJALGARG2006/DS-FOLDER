'''Problem Statement
Employee Payroll Management System
Design and implement an Employee Payroll Management System using Object Oriented Programming (OOPS) concepts.
System Requirements:
Create an abstract class Employee that contains:
Employee ID
Employee Name
Basic Salary
An abstract method calculate_salary().
Implement encapsulation by keeping data members private/protected and providing appropriate getter and setter methods.
Create two derived classes using inheritance:
PermanentEmployee
ContractEmployee
Override the calculate_salary() method in both derived classes to demonstrate polymorphism:
Permanent employee salary includes basic salary + allowances.
Contract employee salary is calculated on hourly basis.
Use runtime polymorphism by creating base class references to derived class objects.
Create a separate class PayrollSystem that:
Stores employee objects.
Displays employee details and calculated salary.
Demonstrate object creation, method calling, and data hiding in the main program.'''


from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, emp_id, name, basic_salary):
        # Protected members
        self._emp_id = emp_id
        self._name = name
        self._basic_salary = basic_salary

    # Getter methods (encapsulation)
    def get_emp_id(self):
        return self._emp_id

    def get_name(self):
        return self._name

    def get_basic_salary(self):
        return self._basic_salary

    # Setter methods (encapsulation)
    def set_emp_id(self, emp_id):
        if not emp_id:
            raise ValueError("Employee ID cannot be empty.")
        self._emp_id = emp_id

    def set_name(self, name):
        if not name:
            raise ValueError("Employee name cannot be empty.")
        self._name = name

    def set_basic_salary(self, basic_salary):
        if basic_salary < 0:
            raise ValueError("Basic salary cannot be negative.")
        self._basic_salary = basic_salary

    @abstractmethod
    def calculate_salary(self):
        pass


class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, basic_salary, allowances):
        super().__init__(emp_id, name, basic_salary)
        self._allowances = allowances

    def get_allowances(self):
        return self._allowances

    def set_allowances(self, allowances):
        if allowances < 0:
            raise ValueError("Allowances cannot be negative.")
        self._allowances = allowances

    def calculate_salary(self):
        return self._basic_salary + self._allowances
    

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, hourly_rate, hours_worked):
        super().__init__(emp_id, name, 0)  
        self._hourly_rate = hourly_rate
        self._hours_worked = hours_worked

    def get_hourly_rate(self):
        return self._hourly_rate

    def set_hourly_rate(self, hourly_rate):
        if hourly_rate < 0:
            raise ValueError("Hourly rate cannot be negative.")
        self._hourly_rate = hourly_rate

    def get_hours_worked(self):
        return self._hours_worked

    def set_hours_worked(self, hours_worked):
        if hours_worked < 0:
            raise ValueError("Hours worked cannot be negative.")
        self._hours_worked = hours_worked

    def calculate_salary(self):
        return self._hourly_rate * self._hours_worked


class PayrollSystem:
    def __init__(self):
        self._employees = []

    def add_employee(self, employee):
        self._employees.append(employee)

    def display_payroll(self):
        print("Payroll Report")
        for emp in self._employees:
            emp_type = type(emp).__name__
            print(f"Type: {emp_type} , ID: {emp.get_emp_id()} , Name: {emp.get_name()} , Salary: {emp.calculate_salary()}")


if __name__ == "__main__":
    payroll = PayrollSystem()

    emp1 = PermanentEmployee("T-103", "trijal", 50000, 10000)
    emp2 = ContractEmployee("C-101", "lui", 150, 120)

    emp1.set_allowances(12000)
    emp2.set_hours_worked(130)

    payroll.add_employee(emp1)
    payroll.add_employee(emp2)

    payroll.display_payroll()
    
class PayrollSystem:
    def display_employee_details(self, employee):
        print("Employee ID:", employee.get_emp_id())
        print("Employee Name:", employee.get_name())
        print("Salary:", employee.calculate_salary())


def main():
    payroll = PayrollSystem()

    emp1 = PermanentEmployee(101, "leon", 30000, 5000)
    emp2 = ContractEmployee(102, "luis", 120, 300)

    payroll.display_employee_details(emp1)
    payroll.display_employee_details(emp2)

if __name__ == "__main__":
    main()

