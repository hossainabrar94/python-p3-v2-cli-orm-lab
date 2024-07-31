from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)


def find_employee_by_name():
    name = input("Enter employee name: ")
    try:
        if employee := Employee.find_by_name(name):
            print(employee)
        else:
            print(f'Employee {name} was not found')
    except ValueError as e:
        print('Value Error: ', e)
        

def find_employee_by_id():
    id_ = input("Enter Employee id: ")
    if employee := Employee.find_by_id(id_):
        print(employee)
    else:
        print(f'Employee {id_} not found')


def create_employee():
    name = input('Enter Employee name: ')
    job_title = input('Enter Employee job title: ')
    department_id = input('Enter Employee department ID: ')
    try:
        department_id = int(department_id)
        employee = Employee.create(name, job_title, department_id)
        print(f'Success {employee}')
    except Exception as e:
        print('Error in creating employee', e)


def update_employee():
    id_ = input("Enter Employee ID: ")
    if employee := Employee.find_by_id(id_):
        try:
            name = input('Enter new name: ')
            job_title = input('Enter new job title: ')
            department_id = input('Enter new department ID: ')
            department_id = int(department_id)
            employee.name = name
            employee.job_title = job_title
            employee.department_id = department_id
            employee.update()
            print(f'Success {employee}')
        except Exception as e:
            print('Error in updating: ', e)
    else:
        print(f'Employee {id_} not found')


def delete_employee():
    id_ = input('Enter Employee ID: ')
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} was deleted')
    else:
        print(f'Employee {id_} was not found')


def list_department_employees():
    department_id = input('Enter Department ID: ')
    if department := Department.find_by_id(department_id):
        employees = department.employees()
        for employee in employees:
            print(employee)
    else:
        print(f'Department {department_id} not found')