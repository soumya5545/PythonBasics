# print("hello")
# try:
#     x=10
# except:
#     print("exception handled")
# print("program completed")

# try:
#     n1,n2=10,5
#     res=n1/n2
#     print(res)
# except ZeroDivisionError:
#     print("thrown ZeroDivision error")
# except SyntaxError:
#     print("synatx error")
# except:
#     print("exception handled")
# else:
#     print("no exception occured")
# finally:
#     print("always execued")

# def enterage(n1):
#     if n1<0:
#         raise ValueError("only integers are allowed")
#     if(n1%2==0):
#         print("even")
#     else:
#         print("odd")
# enterage(-1)

# def enterage(n1):
#     if n1<0:
#         raise ValueError("only integers are allowed")
#     if(n1%2==0):
#         print("even")
#     else:
#         print("odd")
# try:
#     enterage(-1)
# except ValueError:
#     print("value error occured and handled")
# print("program completed")