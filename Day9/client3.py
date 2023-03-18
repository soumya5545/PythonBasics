import sys
sys.path.append("D:/pythonProject/pythonTraining/Day9/package1")
sys.path.append("D:/pythonProject/pythonTraining/Day9/package2")
import emp
import stu
obj1=emp.Employee(1,"soumya,10000")
obj2=stu.Student(5,"patil")
obj1.disemp()
obj2.disStu()