class EmobilisStudent:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hello_me(self):
        print(f"my name is {self.name} and im {self.age} years old")
#creating an object
myobj=EmobilisStudent("carol", 17)
myobj2=EmobilisStudent("joy", 18)
myobj.hello_me()
myobj2.hello_me()

#magari
class Magari:
    def __init__(self,model,year):
        self.model=model
        self.year=year
    def hello_me(self):
        print(f"toyota {self.model} made in {self.year}")


#creating an object
myobj=Magari("volvo" ,2015)
myobj.hello_me()
myobj=Magari("mazda",2017)
myobj.hello_me()
myobj=Magari("audi" ,2021)
myobj.hello_me()


class hostels:
    def __init__(self,name,students,prefect,):
        self.name=name
        self.students=students
        self.prefect=prefect
    def hello_me(self):
        print(f"The cleanest house is {self.name} it accomodates {self.students} students and the house prefect is {self.prefect}")
myobj=hostels("Everest dorm",600 ,"vidar hassan")
myobj.hello_me()
