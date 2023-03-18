#single inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print("parent")
# class B(A):
#     def m2(self):
#         print("child")
# obj=B()
# obj.m1()
# obj.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=50,10
#     def m2(self):
#         print(self.a-self.b)
# obj=B()
# obj.m1()
# obj.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=50,10
#     def m2(self):
#         print(self.a-self.b)
# class C(B):
#     i,j=50,10
#     def m3(self):
#         print(self.i*self.j)
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=50,10
#     def m2(self):
#         print(self.a-self.b)
# class C(A):
#     i,j=50,10
#     def m3(self):
#         print(self.i*self.j)
# obj=C()
# obj.m1()
# obj.m3()
# obj=B()
# obj.m1()
# obj.m2()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B:
#     a,b=50,10
#     def m2(self):
#         print(self.a-self.b)
# class C(A,B):
#     i,j=50,10
#     def m3(self):
#         print(self.i*self.j)
# obj=C()
# obj.m1()
# obj.m2()
# obj.m3()

# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
# class B(A):
#     a,b=50,10
#     def m1(self):
#         super().m1()
#         print(self.a-self.b)
# obj=B()
# obj.m1()

# class A:
#     a,b =10,20
# class B(A):
#     x,y=30,40
#     def m1(self):
#         i,j=10,50
#         print(i+j)
#         print(self.x+self.y)
#         print(self.a+self.b)
# obj=B()
# obj.m1()

# class A:
#     name="soumya"
# class B(A):
#     names="patil"
# obj=B()
# print(obj.names)

# class A:
#     name="soumya"
# class B(A):
#     name = "patil"
#     def m1(self):
#         print(super().name)
#
# obj=B()
# obj.m1()
# print(obj.name)


