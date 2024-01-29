#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


print("hello")


# In[18]:


#string operations
#we can perform the various operations on a string 
#like [:][1:2] like 
#1)indexing 2)string methods 3)string functions/*

#string indexing
a="sanjivani"
print(type(a))
print(a[2:3])
print(a[:])
print(a[:4])
print(a[3:])

#functions like input := input is a function or we can say it is a keyword which is going to take the input from user
a=int(input("Enter the number"))
b=int(input("Enter the number"))
print(a)
#operations on numbers like addition ,substraction,multi,division
print(a+b," ",a-b, " ", a*b ," ", a/b)

#string methods like slice ,strip,upper,lower,count,len
x=string(input("Enter name"))



# In[ ]:


#left shift and right shift operators


# In[30]:


x=10
y=5
z=x & y
print(z)
z1= x | y
print(z1)
z2= x^ y
print(z2)
a=1
print(x<<1)  #moves one time to the left side so ans is 20
print(x>>y)


# In[45]:


#program for shallow copy and deep copy
#1st program for shallow copy
print()
print("below list is shallow copy")
print()
import copy
original_list=[1,2,[3,4],5]
print("original list is",original_list)
shallow_copy=copy.copy(original_list)
print("original list is",original_list)
print("shallow copy list is",shallow_copy)
shallow_copy[2][0]=99
print("original list is",original_list)
print("shallow copy list is",shallow_copy)

#2nd program for deep copy
print()
print("below list is deep copy")
print()
import copy
original_list=[1,2,[3,4],5]
print("original list is",original_list)
deep_copy=copy.deepcopy(original_list)
print("original list is",original_list)
print("shallow copy list is",deep_copy)
deep_copy[2][0]=99
print("original list is",original_list)
print("deep copy list is",deep_copy)



# In[61]:


#program for functions like 1)simple functions 2)nested functions

#1.program for nested functions

def greet():
  def sey_hello():
        print("hello")
  return sey_hello
myfunction=greet()
myfunction()

print()
#2.program for simple function

def greet():
  print("world")

myfunc=greet
myfunc()

#3 execute function
def greet():
    print("hello")
def execute_function(func):
   func()
execute_function(greet)



# In[69]:


#lambda is a customizable function
#a,b are  the variables
#perform operations using lambda function

multiply =lambda a,b :a*b
res=multiply(2,3)
print ("multiplication is:", res)

add=lambda a,b:a+b
res=add(3,4)
print("Addition is:", res)

sub=lambda a,b:a-b
res=sub( 6,1)
print("Substraction is:",res)

div=lambda a,b:a/b
res=div(4, 2)
print("division is:",res)


# In[76]:


#lambda +composed 
def substract(a,b):
  return a-b
def perform_op(op,x,y):
 return op(x,y)
res=perform_op(add,5,3)
print(res) #output

res=perform_op(substract,8,4)
print(res)
def square(x):
 return x*x
w
def compose(f,g):
    return lambda x,y:f(g(x,y))
res=compose(square,add)(2,3)
print(res)


# In[79]:



def compose(f,g):
    return lambda x,y:f(g(x,y))
res=compose(square,add)(2,3)
print(res)


# In[84]:


#implement the arithmetic operations using dictionary (keys ,values) pairs

def add(a,b):
 return a+b
def sub(a,b):
 return a-b
def multi(a,b):
 return a*b
def div(a,b):
 return a/b

ope={
    "+":add,
    "-":sub,
    "*":multi,
    "/":div}
user=(input("Enter which operation you want to do(+,-,*,/):"))
b=int(input("Enter 1st no"))
c=int(input("Enter 2nd no"))
if user in ope:
    res=ope[user](b,c)
    print(res)
else:
    print("invalid operator")



# In[6]:


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
result =factorial(5)
print(result)
n=16
print(n)
print(factorial(1))

a={2:2}
print(type(a))


# In[35]:


a = {"a": 6, "b": 4, "c": 1}

# Sorting the dictionary by values in ascending order
sorted_dic = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}
print(sorted_dic)

# Sorting the dictionary by values in ascending order with print instructions
print("Printing instructions:", {k: v for k, v in sorted(a.items(), key=lambda item: item[1])})

# Sorting the dictionary by values in descending order with print instructions
print("Printing instructions:", {k: v for k, v in sorted(a.items(), key=lambda item: item[1], reverse=True)})


# In[60]:


students=[{"name":"abc","age":19,"grade":56},{"name":"bbc","age":20,"grade":89},{"name":"ddf","age":21,"grade":67}]
print("list of student is:",stud)
print()

total_age=sum(student['age'] for student in students)
avg_age=total_age/len(students)
print("average age is:",avg_age)
print()
high_grade=max(students,key=lambda x:x["grade"])
print("highest grade is:",high_grade)

stud_new_dict={student["name"]:student["age"]for student in students}
print()
print("new dictionary where keys are students and values are their ages =",stud_new_dict)


# In[63]:


#set
#set includes only the unique values it does not include the duplicate values
#set does not have index(i.e we cant access set element by its inde)
def process_set(items):
    for item in items:
        print(item)
my=[1,2,3,4]
print(my[0])
        


# In[70]:


#priting stars

for i in range(0,4):

    for j in range(4-i):
    
        print("*",end="")
    
    print()


# In[ ]:


#next class portfolio
#connecting files in same folder using import
#ans of que which is given in grp pdf

