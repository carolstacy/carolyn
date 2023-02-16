#hello function
def hello():
    print("this is my first function")
hello()
hello()
#calculate function
def calculate():
    x=5
    y=3
    print(x*y)
calculate()
#name function
def majina(fname,lname):
    print(fname+ " "+lname)
majina("carol", "njambi")
majina("joyangel", "stacy")
majina("jeremy", "zikki")
majina("edith" ,"chirii")
#greetings fuction
def greetings(name, greeting="hello"):
    print(greeting +" "+ name)
greetings("caroll")
greetings("niaje", "njambi")
greetings("joan", "ssup")

#comment function
def comments(form4, comment="congrats"):
    print(comment +" "+form4)
comments("form4 red")
comments("form4 green", "kongole")

#maximum function
def maxvalue(a,b,c,d,e,f):
    return max(a,b,c,d,e,f)
result=maxvalue(7,9,1,8,17,45)
print(result)
#min function
def minvalue(p,q,r,s,t,u,v):
    return min(p,q,r,s,t,u,v)
result=minvalue(23,8,7,28,12,29,36)
print(result)
#sorting function
def sort_list(lst):
    return sorted(lst)
answer=sort_list([3,9,0,2,7,1,5,4,2])
print(answer)
 #print function
 def print_numbers(n):
     for i in range(n):
         print(i)
 print_numbers(5)