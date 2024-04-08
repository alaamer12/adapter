class Employee:
    def __init__(self, username, name, salary, hours_worked):
        self.username = username
        self.payitems = {"name": name, "salary": salary, "hours_worked": hours_worked}

    def calculate_bonus(self):
        # Assume a simple bonus calculation based on salary
        return self.payitems['salary'] * 0.1  # 10% of salary

    def calculate_overtime_pay(self, hourly_rate):
        standard_hours = 40
        hours_worked = self.payitems['hours_worked']
        if hours_worked > standard_hours:
            overtime_hours = hours_worked - standard_hours
            return overtime_hours * hourly_rate * 1.5  # Overtime rate is 1.5 times the hourly rate
        else:
            return 0

    def calculate_tax(self):
        # Assume a simple tax calculation based on salary
        return self.payitems['salary'] * 0.2  # 20% tax rate

    def calculate_deductions(self):
        # Assume a fixed deduction amount
        return 1000

    def calculate_benefits(self):
        # Assume a fixed benefits amount
        return 500