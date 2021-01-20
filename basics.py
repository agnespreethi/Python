#conditional logic

a = True
if a:
    print('hi')        # print
else:
    print('bye')
print('----------------------------------------')

a = True
if a:
    print('hi')         # print
else:
    print('bye')
print('jesus')          # print (out of if condition)
print('----------------------------------------')

a = False
b = True
if a:                   # a-false
    print('hi')
else:
    print('bye')        # print b-true
print('jesus')          # print (out of if condition)
print('----------------------------------------')

a = True
b = True
if a:
    print('hi')         # print a and b are true
elif b:
    print('preethi')
else:
    print('bye')
print('----------------------------------------')

a = False
b = True
if a:                   # a-false
    print('hi')
elif b:
    print('preethi')    # print b-true
else:
    print('bye')
print('----------------------------------------')

a = False               # a-false
b = False               # b-false
if a:
    print('hi')
elif b:
    print('preethi')
else:
    print('bye')         # print
print('----------------------------------------')

#truthy and falsy  

print(bool(''))         #falsy
print(bool(0))          #falsy
print('----------------------------------------')

a = 'hello'             #converts into bool-true
b = 5                   #converts into bool-true
if a and b:
    print('hai')        # print
else:
    print('bye')
print('----------------------------------------')

# falsy
# None,False,0,0.0,0j,Decimal(0),Fraction(0, 1),[] - an empty list,{} - an empty dict,() - an empty tuple,'' - an empty str,b'' - an empty bytes,set() - an empty set,an empty range, like range(0)
# objects for which ---> obj.__bool__() returns False , obj.__len__() returns 0   

#ternary operator

employee = True
entry="allow" if employee else "not allow"
print(entry)
print('----------------------------------------')

#short circuting

students = True
others = False
if students or others:
    print("students are allowed to write exams")
print('----------------------------------------')
students = True
parents = True
if students and parents:
    print("students and parents are allowed to attend the meeting")
print('----------------------------------------')

#logical operators- <,>,==,<=,>=,!=

print(4 > 5)
print('a' > 'b')
print('a' > 'A')
print(1 < 2 < 3 < 4)
print(1 < 2 > 3 < 4)
print(4 <= 5)
print(5 == 5)
print(6 != 8)
print('----------------------------------------')

# is VS == ((is) keyword)

print(True == 1)
print('1' == 1)
print([] == 1)
print([] == [])
print(10 == 10.0)
print([1,2,3] == [1,2,3])
print('----------------------------------------')
print(True is 1)             # different values 
print('1' is 1)              # different values 
print([] is 1)               # different values 
print([] is [])              # same list but has different memory location
print(10 is 10.0)            # different values 
print([1,2,3] is [1,2,3])    # same list but has different memory location
print('----------------------------------------')
print(True is True)
print('1' is '1')
print([] is [])             #same list but has different memory location
print(1 is 1)
print(10 is 10)
print([1,2,3] is [1,2,3])   #same list but has different memory location
print('----------------------------------------')
a = [1,2,3]
b = [1,2,3]
print(a is b)               #same list but has different memory location
print(a == b)
print('----------------------------------------')

#for loop

for x in [1,2,3]:
    print(x)
print('----------------------------------------')
for x in (1,2,3):
    print(x)
print('----------------------------------------')
for x in {1,2,3}:
    print(x)
print('----------------------------------------')
for x in 'preethi':
    print(x)
print('----------------------------------------')
for x in [1,2,3]:
    for y in ['a','b','c']:
        print(x)
print('----------------------------------------')

#iterables

x = {
    'name' : 'pree',
    'age'  : 21,
    'is_vote' : True

}
for y in x:
    print(y)
print('----------------------------------------')
for y in x.items():
    print(y)
print('----------------------------------------')
for y in x.values():
    print(y)
print('----------------------------------------')
for y in x.keys():
    print(y)
print('----------------------------------------')
for y in x.items():
    key,value = y;
    print(key,value)
print('----------------------------------------')
for key,value in x.items():
    print(key,value)
print('----------------------------------------')

#counter

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item
print(counter)
print('----------------------------------------')

#range

print(range(0,5))
print('----------------------------------------')
for i in range(0,10):
    print(i)
print('----------------------------------------')
for _ in range(3):
    print(list(range(5)))
print('----------------------------------------')

#enumerate()

for i,char in enumerate("hello"):
    print(i,char)
print('----------------------------------------')
for i,char in enumerate(list(range(10))):
  print(i,char)
  if char == 5:
    print(f"index of 5 is:{i}")
print('----------------------------------------')

#while

i = 0
while i < 5:
    print('hi')
    i +=1
print('----------------------------------------')
i = 0
while i < 5:
    print('hi')
    i +=1
else:
    print('bye')
print('----------------------------------------')   
i = 0
while i < 5:
    print('hi')
    i +=1
    break
else:
    print('bye')
print('----------------------------------------')
while True:
    input("jesus ")
    break
print('----------------------------------------')
while True:
    s = input("jesus ")
    if(s == 'pree'):
        break
print('----------------------------------------')

# GUI

x = [
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1],
  [1,1,1,1]
]
for y in x:
  for z in y:
    if (z == 1):
      print("*",end=' ')
    else:
      print(" ",end=' ')  
  print(' ')

a=input()

x = [
  [0,1,1,0],
  [1,0,0,1],
  [1,0,0,1],
  [0,1,1,0]
]
for y in x:
  for z in y:
    if (z == 1):
      print("*",end=' ')
    else:
      print(" ",end=' ')  
  print(' ')

a=input()

x = [
  [0,1,1,0],
  [1,0,0,1],
  [1,1,1,1],
  [1,0,0,1],
  [1,0,0,1]
]
for y in x:
  for z in y:
    if (z == 1):
      print("*",end=' ')
    else:
      print(" ",end=' ')  
  print(' ')
print('----------------------------------------')  

#duplicates

a = ['a','b','b','c','d','n','n']
for b in a:
  if a.count(b)>1:
     print(b)
print('----------------------------------------') 
a = ['a','b','b','c','d','n','n']
c = []
for b in a:
  if a.count(b)>1:
    if b not in c:
      c.append(b)
print(c)
print('----------------------------------------') 
a = ['a','b','b','c','d','n','n']
c = []
for b in a:
  if a.count(b)>1:
      c.append(b)
print(c)
print('----------------------------------------') 

# functions

def x():
  print('hello')
x()
print('----------------------------------------') 
def x():
  print('hello')
x()
x()
x()
print('----------------------------------------')

# aruguments and parameters

def x(name,emoji):             # parameters
  print(f'hello {name} {emoji}')
x('agi','😀')                  # arguments
print('----------------------------------------')  

# default parameters and keyword arguments

def x(name='pree',emoji='😀'):
    print(f'hello {name} {emoji}')
x('agi','😀')                    #parameters
x('preethi','😀')                #parameters

x(name='jesus',emoji='😀')       #keywords
x(emoji='😀',name='jesus')       #keywords
x()                              
x(name='baby')                   #keywords
print('----------------------------------------')

#return - keyword

def sum(num1,num2):
    def another_func(num1,num2):
        return num1+num2
    return another_func(num1,num2)
    return 5
    print('hello')
total = sum(10,20)
print(total)
print('----------------------------------------')

#docstring

def test(a):
    '''
     Info: this function tests and prints parameter a
    '''
    print(a)
test('!!!')
help(test)
print(test.__doc__)
print('----------------------------------------')

#special characters - *args,**kwargs

def super_func(*args, **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func(1,2,3,4,5, p=5,q=10))
print('----------------------------------------')
def super_func(name, *args, i='hi', **kwargs):
    total = 0
    for items in kwargs.values():
        total += items
    return sum(args) + total
print(super_func("Agi", 1,2,3,4,5, t=5,u=10))
print('----------------------------------------')

#global keyword

total = 0
def count(total):
    total += 1
    return total
print(count(count(count(total))))
print('----------------------------------------')

#nonlocal - keyword

def outer():
    x = "local"
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer()    
print('----------------------------------------')
def outer():
    x = "local"
    def inner():
        x = "nonlocal"
        print("inner:",x)
    inner()
    print("outer:",x)
outer() 
print('----------------------------------------')
