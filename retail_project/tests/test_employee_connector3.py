from retail_project.connector.employee_connector import EmployeeConnector
from retail_project.models.employee import Employee

ec = EmployeeConnector()
ec.connect()
emp = Employee()
emp.ID = 6
emp.EmployeeCode = "EMP888"
emp.Name = "Pikachu"
emp.Phone = "113"
emp.Email = "pikachu@gmail.com"
emp.Password = 456
emp.IsDeleted = 0

result = ec.update_one_employee(emp)
if result > 0:
    print("Chúc mừng bà nha, đã thêm thành công")
else:
    print("Thật đáng tương")
