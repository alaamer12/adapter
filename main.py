from employee import Employee


class Payroll:
    def calculate_payroll(self, employees, hourly_rate):
        print("Calculating Payroll")
        for employee in employees:
            print(f"Payroll for {employee.employee.payitems['name']}:")
            print(f"- Base Salary: {employee.employee.payitems['salary']}")
            overtime_pay = employee.calculate_overtime_pay(hourly_rate)
            print(f"- Overtime Pay: {overtime_pay}")
            bonus = employee.calculate_bonus()
            print(f"- Bonus: {bonus}")
            tax = employee.calculate_tax()
            print(f"- Tax: {tax}")
            deductions = employee.calculate_deductions()
            print(f"- Deductions: {deductions}")
            benefits = employee.calculate_benefits()
            print(f"- Benefits: {benefits}")
            total_pay = (employee.employee.payitems['salary'] + overtime_pay + bonus +
                         benefits) - (tax + deductions)
            print(f"- Total Pay: {total_pay}")


class EmployeeAdapter:
    def __init__(self, employee):
        self.employee = employee


    @property
    def name(self):
        return self.employee.payitems['name']

    @property
    def salary(self):
        return self.employee.payitems['salary']

    def calculate_bonus(self):
        return self.employee.calculate_bonus()

    def calculate_overtime_pay(self, hourly_rate):
        return self.employee.calculate_overtime_pay(hourly_rate)

    def calculate_tax(self):
        return self.employee.calculate_tax()

    def calculate_deductions(self):
        return self.employee.calculate_deductions()

    def calculate_benefits(self):
        return self.employee.calculate_benefits()


# Example usage
employee1 = Employee("user1", "John Doe", 5000, 45)
employee2 = Employee("user2", "Jane Smith", 6000, 38)

payroll = Payroll()
employees = [EmployeeAdapter(employee1), EmployeeAdapter(employee2)]
hourly_rate = 20  # Assuming an hourly rate for overtime calculation
payroll.calculate_payroll(employees, hourly_rate)
