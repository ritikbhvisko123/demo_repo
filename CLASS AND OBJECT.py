"Object oriened programing class and object"

"classes - instance of class"
"Templete -- it is fix thing like a applicton letter date is already written in the format" \
"DRY - do not repeat yourself "

# class student:
#     pass
# Ritik=student
# Tanuj=student
# Ritik.name="Ritik Bhawsar"
# Tanuj.name="Tanuj Sonare"
# Ritik.couse="B.Tech(M.E.)"
# Tanuj.course="B.Tech(C.S.)"
# Tanuj.marks_12="85%"
# Ritik.marks_12="85%"
# print(Ritik,Tanuj.course)
# print(Ritik.marks_12)

# class Employee:
#     no_of_leaves=8
#     pass
# Ritik=Employee()
# Tanuj=Employee()
# Ritik.name="Ritik Bhawsar"
# Tanuj.name="Tanuj Sonare"
# Ritik.salary=30000
# Tanuj.salary=45000
# Ritik.position="jr.engineer"
# Tanuj.position="jr.software engineer"
# # Ritik.no_of_leaves=10
# print(Ritik.no_of_leaves)
# # Employee.no_of_leaves=12
# print(Employee.no_of_leaves)
# print(Ritik.__dict__)


# class Employee:
#     no_of_leaves=8
#     def printdetails(self):
#         return f"Name is {self.name}  salary is {self.salary} and position is {self.position}"
#
# Ritik=Employee()
# Tanuj=Employee()
# Ritik.name="Ritik Bhawsar"
# Tanuj.name="Tanuj Sonare"
# Ritik.salary=30000
# Tanuj.salary=45000
# Ritik.position="jr.engineer"
# Tanuj.position="jr.software engineer"
# print(Ritik.printdetails())

#

"constructor"
# class Employee:
#     no_of_leaves=8
#     def __init__(self,aname,asalary,aposition,percentage):
#         self.name=aname
#         self.salary=asalary
#         self.position=aposition
#         self.percentage=percentage
#
#         # def printdetails(self):
#         #     return f"Name is {self.name}  salary is {self.salary} and position is {self.position}"
# Ritik=Employee("Ritik Bhawsar",30000,"jr. engineer","76%")
# Tanuj=Employee("Tanuj Sonare",45000,"jr.software engineer","85%")
# #
# Ritik=Employee()
# Tanuj=Employee()
# Ritik.name="Ritik Bhawsar"
# Tanuj.name="Tanuj Sonare"
# Ritik.salary=30000
# Tanuj.salary=45000
# print(Tanuj.__dict__)



# class Employee:
#     no_of_leaves=8
#     def __init__(self,aname,asalary,aposition,percentage):
#         self.name=aname
#         self.salary=asalary
#         self.position=aposition
#         self.percentage=percentage
#
#     def printdetails(self):
#         return f"Name is {self.name}  salary is {self.salary} and position is {self.position}"
#
#     @classmethod
#     def change_leaves(cls, nowleaves):
#         cls.no_of_leaves = nowleaves
#
# there is no way to create and understanding the culture and management and during the analysis and fundamental of the writtentes
# Ritik=Employee("Ritik Bhawsar",30000,"jr. engineer","76%")
# Tanuj=Employee("Tanuj Sonare",45000,"jr.software engineer","85%")
#
# Ritik.change_leaves(45)
# print(Ritik.no_of_leaves)
# print(Tanuj.no_of_leaves)



# class student:
#     def __init__(self, aname, acourse, agrade, a_living_city):
#         self.name = aname
#         self.course = acourse
#         self.grade = agrade
#         self.living_city = a_living_city
#
#
# Ritik = student("Ritik Bhawsar", "B.Tech(M.E.)", "8.3 CGPA", "INDORE")
# Tanuj = student("Tanuj Sonare", "B.Tech(C.S.)", "8.23 CGPA", "INDORE")
# Siddharth = student("Siddharth Agnihotri", "B.COM", 80, "INDORE")
# Prateek = student("Prateek Chawda", "B.COM", 78, "INDORE")
# print(Ritik.__dict__)





# class student:
#     no_of_leaves=8
#     def __init__(self, aname, acourse, agrade, a_living_city):
#         self.name = aname
#         self.course = acourse
#         self.grade = agrade
#         self.living_city = a_living_city
#
#     @classmethod
#     def from_str(cls,string):
#         # params=string.split("-")
#         # print(params)
#         # return cls(params[0],params[1],params[2],params[3])
#         return cls(*string.split("-"))  # one liner function
# Ritik = student("Ritik Bhawsar", "B.Tech(M.E.)", "8.3 CGPA", "INDORE")
# Tanuj = student("Tanuj Sonare", "B.Tech(C.S.)", "8.23 CGPA", "INDORE")
# Siddharth=student.from_str("Siddharth Agnohotri-B.COM-80%-INDORE")
# print(Siddharth.grade)
# print(Siddharth.__dict__)
# print(Siddharth.no_of_leaves)




# class student:
#     no_of_leaves=8
#     def __init__(self, aname, acourse, agrade, a_living_city):
#         self.name = aname
#         self.course = acourse
#         self.grade = agrade
#         self.living_city = a_living_city
#         def from_str(cls,string):
#             # params=string.split("-")
#             # print(params)
#             # return cls(params[0],params[1],params[2],params[3])
#             return cls(*string.split("-"))  # one liner function
#         @staticmethod
#         def printgood(string):
#             print('this is job'+string)
# Ritik = student("Ritik Bhawsar", "B.Tech(M.E.)", "8.3 CGPA", "INDORE")
# Tanuj = student("Tanuj Sonare", "B.Tech(C.S.)", "8.23 CGPA", "INDORE")
# Siddharth=student.from_str("Siddharth Agnohotri-B.COM-80%-INDORE")




'''ABSTRACTION AND IMCAPSULATION(hide implementation details)'''
'''inheritance'''

# class Employee:
#     no_of_leaves=9
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#     def printdetails(self):
#         return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"
#     @classmethod
#     def change_leaves(cls,nowleaves):
#         cls.no_of_leaves=nowleaves
#
#     @classmethod
#     def from_dash(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good",+ string)



# class programmer(Employee):
#     def __init__(self,aname,asalary,arole,languages):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.language=languages
#     def printprog(self):
#         return f"The programmer's name is  {self.name} salary is {self.salary} and role is {self.role} and languages{self.language} is"
# harry=Employee("Harry",255,"Instructor")
# rohan=Employee("Rohan",400,"student")
# shubham=programmer("shubham",555,"programmer",['python'])
# karan=programmer("karan",777,"programmer",['python'])
# print(karan.printprog())



# class student:
#     def __init__(self,aname,agender,acourse,asituation,aachivements):
#         self.name=aname
#         self.gender=agender
#         self.course=acourse
#         self.situation=asituation
#         self.achivements=aachivements
# Ritik=student("Ritik Bhawsar","Male","B.TECH(M.E.)","COMPLETED IN 2022","RUNNNER UP OF MECHQUIZ COMPETETION")
# Siddharth=student("Siddharth Agnihortri","Male",'B.COM',"COMLETED IN 2021","PARTICIPATED IN SPEACH IN SCHOOL")
# Prateek=student("Prateek Chawda","Male","B.COM","COMPLETED IN 2021", "PARTICIPATED IN SCHOOL SPORTS AND ART COMPETITION")
# print(Ritik.gender,Ritik.name)
# print(Prateek.__dict__)



#
# class Dad:
#     basketball=4
#     # print(basketball)
#
# class Son(Dad):
#     dance=1
#     basketball = 7
#     def isdance(self):
#         return f"yes I dance {self.dance} no of times"
# class Grandson(Son):
#     dance = 6
#     # def isdance(self):
#     #     return f"Jackson yeah!" f"Yes I dance very awesomely {self.dance} no of times"
#
# darry=Dad()
# larry=Son()
# harry=Grandson()
# print(harry.isdance())
# print(harry.basketball)


"class making of three electronic device,pocket gadget,phone"


'''public protected private'''
#
#
# class Employee:
#     no_of_leaves=9
#     _protect=11
#     __private=98
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#     def printdetails(self):
#         return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"
#     @classmethod
#     def change_leaves(cls,nowleaves):
#         cls.no_of_leaves=nowleaves
#
#     @classmethod
#     def from_dash(cls,string):
#         return cls(*string.split("-"))
#
#     @staticmethod
#     def printgood(string):
#         print("This is good",+ string)
# harry=Employee("Harry",255,"Instructor")
# rohan=Employee("Rohan",400,"student")
# print(Employee._protect)
# # print(Employee.__private)
# # emp=Employee()
# print(harry._Employee__private)

# "polymorphism"
# print(5+6)
# print("5"+"6")

#
# class A:
#     classvar1="I am a class variable in class A"
#     def __init__(self):
#         # self.var1="I am inside class A's constructor"
#         self.classvar1="Instancce var in class A"
#         self.special="special"
# class B(A):
#     classsvar1="I am in class B"
#
#     def __init__(self):
#         # super().__init__()# ab error nnahi hoga
#         self.var1 = "I am inside class B's constructor" # ISKO LAGANE SE UPAR KA FUNCTION OVERWRITE HOGAYA HAI
#         self.classvar1 = "Instancce var in class B"
#         super().__init__()
# a=A()
# b=B()
# print(b.classvar1)
# #print(b.special)# overrite hone ki wajah se ye nahi error dega
# print(a.var1)
# print(b.special)


"diamond problem"
#
# class A:
#     def met(self):
#         print("This is a method from class A")
#
#
# class B(A):
#     def met(self):
#         print("This is a method from class B")
#
#
# class C(A):
#     def met(self):
#         print("This is a method from class C")


# class D(C,B):
#     pass

#
# a=A()
# b=B()
# c=C()
# d=D()
# print(d.met())
#
#
# class Employee:
#     no_of_leaves=9
#
#     def __init__(self,aname,asalary,arole):
#         self.name=aname
#         self.salary=asalary
#         self.role=arole
#
#     def printdetails(self):
#         return f"The Name is {self.name} salary is {self.salary} and role is {self.role}"
#
#     @classmethod
#     def change_leaves(cls,nowleaves):
#         cls.no_of_leaves=nowleaves
#
#     '''MAPPPING OPERATORS'''
#     def __add__(self, other):
#         return self.salary+other.salary
#
#
# emp=Employee("Harry",345,"programmer")
# emp1=Employee("Rohan",145,"cleaner")
# print(emp+emp1)
# print(emp/emp1)


# from abc import ABCMeta, abstractmethod
# from abc import ABC
# class Shape(metaclass=ABCMeta):
#     @abstractmethod
#     def printarea(self):
#         return 0


# class Rectangle:
#     type="Rectangle"
#     sides=4
#     def __init__(self):
#         self.lenght=6
#         self.breadth=10
#     def printarea(self):
#         return self.length * self.breadth
# rect=Rectangle()
# print(rect.lenght)



# #
# class Employee:
#     def __init__(self,fname,lname):
#         self.fname=fname
#         self.lname=lname
#         # self.email=email
#         # self.email=f"{fname}.{lname}@codewithharry.com"
#
#
#     @property
#     def explain(self):
#         return f"This employee is {self.fname} {self.lname}"
#
#     @property
#     def email(self):
#        return f"{self.fname}.{self.lname}@codewithharry.com"
#
#     @email.setter
#     def email(self,string):
#         print("setting.now...")
#
#         names=string.split("@")[0]
#         self.fname=names.split(".")[0]
#         self.lname=names.split(".")[1]
# #
#
# hindustani_supporter=Employee("Hindustani","supporter")
# nikhil_raj_pandey=Employee("Nikhil","Raj")
# hindustani_supporter.fname="US"
#
# # print(hindustani_supporter.explain())   #() braket lagane par hi chalega ye
# # print(hindustani_supporter.email())
#
# print(hindustani_supporter.explain) # ye bina () ke bhi run hoga kyunki @property fucntion laga hai upper isme
# print(hindustani_supporter.email)
#
# hindustani_supporter.email="this.that@codewithharry.com"
# print(hindustani_supporter.lname)
# print(hindustani_supporter.fname)
# print(hindustani_supporter.email)
#
# del hindustani_supporter.email  #deleting


# class Employee():
#     pass
#
# print(id("this is game"))
# oo="this is gamee"
# print(dir(oo))


# import inspect
# print(inspect.getmembers(Employee))




'''mini project '''
'create a library class'
"displaybook" \
"lend book" \
"add book" \
"return book"




"generators"
# iterable - __iter__()or __getitem__()
# Iterator - __next__()
# Iteration
#
# for i in range(780000000000):
#     print(i)
# #
# def gen(n):
#     for i in range(n):
#         # return i
#         yield i
#
#
# g=gen(2)
# print(g.__next__())
# print(g.__next__())
#
# h=3435
# h="harry"
# ier=iter(h)
# print(ier.__next__())
# print
# for c in h:
#     print(c)


'''list comprehension'''
# ls=[]
# for i in range(100):
#     if i%3==0:
# #         ls.append(i)
# ls=[i for i in range(100) if i%3==0]
# print(ls)
#
# # dict1={i:f"item {i}" for i in range(1,100) if i%10==0}
# dict1={i:f"item {i}" for i in range(1,5)}
# dict2={value:key for key,value in dict1.items()}
# print(dict1,"\n",dict2)
# # print(dict1)
print("hello")

class f:
    def __init__(self,name,age):
        self.name=name
        self.age=age
ritik=f('RITIK BHAWSAR',23)
nitesh=f('NITESH RATHORE',20)
print(ritik.__dict__)


print("hello")