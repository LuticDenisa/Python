class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def display_info(self):
        return f"Employee ID: {self.employee_id}\nName: {self.name}"

class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id)
        self.salary = salary
        self.department = department

    def display_info(self):
        return f"{super().display_info()}\nRole: Manager\nSalary: ${self.salary}\nDepartment: {self.department}"

    def manage_team(self):
        return "Managing the team and projects."

class Engineer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id)
        self.salary = salary
        self.programming_language = programming_language

    def display_info(self):
        return f"{super().display_info()}\nRole: Engineer\nSalary: ${self.salary}\nProgramming Language: {self.programming_language}"

    def write_code(self):
        return "Writing code and developing software."

class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, sales_target):
        super().__init__(name, employee_id)
        self.salary = salary
        self.sales_target = sales_target

    def display_info(self):
        return f"{super().display_info()}\nRole: Salesperson\nSalary: ${self.salary}\nSales Target: ${self.sales_target}"

    def meet_sales_target(self):
        return "Meeting sales targets and building client relationships."


manager = Manager("Ioana", 1, 8000, "Marketing")
print(manager.display_info())
print(manager.manage_team())

engineer = Engineer("Mihai", 2, 10000, "C#")
print(engineer.display_info())
print(engineer.write_code())

salesperson = Salesperson("Cristi", 3, 2700, 20000)
print(salesperson.display_info())
print(salesperson.meet_sales_target())
