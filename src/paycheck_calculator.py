#program to calculate employee pay checks based on regular hours and overtime
employee_name = input("Enter employee name: ")
regular_hours = float(input("Enter regular hours worked: "))
overtime_hours = float(input("Enter overtime hours worked: "))
regular_pay = 20
overtime_pay = 30

if regular_hours <=40 and overtime_hours ==0:
    employee_salary = regular_pay * regular_hours
elif regular_hours > 40 and overtime_hours > 0:
    employee_salary = (regular_pay * 40) + (overtime_pay * overtime_hours)
else:
    employee_salary = (regular_pay * regular_hours) + (overtime_pay * overtime_hours)
print(f"{employee_name}'s salary is ${employee_salary:.2f}")


# === Constants ===
REGULAR_RATE = 20
OVERTIME_RATE = 30
REGULAR_HOURS_LIMIT = 40




# === References ===
# zybooks.
