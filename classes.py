#!/usr/bin/python3.6
# _*_ coding: utf-8 _*_
"""

SYNOPSIS

    Classes tutorials - Corey Shafer

DESCRIPTION

    https://www.youtube.com/watch?v=ZDa-Z5JzLYM

"""

class Employees:

    num_employees = 0                         # Class Variable - Shared by all instances
    raise_amount = 1.04                      # Class variable - Shared by all instances
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employees.num_employees += 1              # Class variable does not change for each instance
                                                 # Same for all employees

    def fullname(self):                          # A method
        return '{} {}' .format(self.first, self.last)

    def apply_raise(self):                                # A method
        self.pay = int(self.pay * self.raise_amount)      # Self used because it is an instance variable
                                                          # Self recieves instance as first argument

    @classmethod                              # Changes class variable raise_amount from outside class
    def set_raise_amount(cls, amount):                    # Passes class method automatically
        cls.raise_amount = amount

    @staticmethod                                         # Static method, does not use self or cls
    def is_weekday(day):                                  # Does not operate n instance or class
        if day.weekday() == 5 or day.weekday == 6:        # uses numbers for days of week, 0=Mon 5=Sat 6=Sun
            return False
        return True

    @staticmethod
    def day_of_week(day):
        if day.weekday() == 0:
            print('Monday')
        elif day.weekday() == 1:
            print('Tuesday')
        elif day.weekday() == 2:
            print('Wedneday')
        elif day.weekday() == 3:
            print('Thursday')
        elif day.weekday() == 4:
            print('Friday')
        elif day.weekday() == 5:
            print('Saturday')
        else:
            print('Sunday')



emp_1 = Employees('Phil', 'Kershaw', 50000)                # An Instance of a class
emp_2 = Employees('Jude', 'Kershaw', 60000)
emp_3 = Employees('James', 'Kershaw', 60000)


Employees.set_raise_amount(1.05)
print('Employees raise amount', Employees.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

# import datetime
# my_date = datetime.date(1961, 2, 26)
# print(Employees.is_weekday(my_date))
# print((Employees.day_of_week(my_date)))

