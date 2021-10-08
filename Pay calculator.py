
salary =   float (input("input your salary: "))
hours_worked =  int (input("input hours worked: "))
standard_work_week = 40
overtime_multiplier = 1.5


if hours_worked > standard_work_week:
    
    overtime = hours_worked - standard_work_week
    total_pay = float((salary) * (hours_worked - overtime)) + (overtime * salary *overtime_multiplier)
    print (total_pay)

else:
    pay_before_taxes= float((salary) * (hours_worked)) 
    print (pay_before_taxes)








