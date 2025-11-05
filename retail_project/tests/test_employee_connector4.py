from retail_project.connector.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.ID = 5

result = ec.delete_one_employee(emp)
if result > 0:
    print("Chúc mừng bà nha, đã xóa thành công")
else:
    print("Thật đáng tương")
