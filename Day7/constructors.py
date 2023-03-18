# class Myclass:
#     def __init__(self):
#         print("constructor")
#     def m1(self):
#         print("method")
# obj=Myclass()
# obj.m1()

# class Myclass:
#     def __init__(self, name):
#         print("constructor",name)
#     def m1(self):
#         print("method")
# obj=Myclass("hello")
# obj.m1()

# class Myclass:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#         print("constructor")
#     def display(self):
#         print(self.eid,self.ename,self.sal)
# obj=Myclass(10153,"soumya",10000)
# obj.display()

# class Myclass:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid
#         self.ename=ename
#         self.sal=sal
#         print("constructor")
#     def __str__(self):
#         return self.ename
# obj=Myclass(10153,"soumya",10000)
# print(obj)