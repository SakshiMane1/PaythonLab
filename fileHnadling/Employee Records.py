with open("employees.txt", "r") as file:
    lines = file.readlines()

employees = []

for line in lines[1:]:
    emp_id, name, department, salary = line.strip().split(",")

    employees.append({
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": float(salary)
    })

# Display all employees
print("All Employees:")

for employee in employees:
    print(employee)

# Highest-paid employee
highest = max(employees, key=lambda x: x["salary"])

print("\nHighest Paid Employee:")
print(highest)

# Average salary
total = sum(employee["salary"] for employee in employees)
average = total / len(employees)

print("\nAverage Salary:", average)

# Employees above given salary
amount = float(input("\nEnter salary limit: "))

print("\nEmployees earning above", amount)

for employee in employees:
    if employee["salary"] > amount:
        print(employee)