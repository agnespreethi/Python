#fundamental - int,float,complex,bool,str,list,tuple,set,dict

#integers and float

print(2+3)   #addition
print(2-3)   #subtraction
print(2*3)   #multiplication
print(2/3)   #division(float quotient)
print(2//3)  #division(int quotient)
print(2**3)  #power
print(2%3)   #division(reminder)

print("------------------------------------")

#type

print(type(8))
print(type(2/4))

print("------------------------------------")

#math functions

print(round(3.1))   #smallest round of
print(round(3.9))   #largest round of
print(abs(-20))     #absolute value of argument(positive)

print("------------------------------------")

from math import *
print(factorial(3)) 
print(fabs(-20))    #float absolute value of argument(positive)   
print(fmod(5,4))    #division(reminder)
print(exp(2))       #exponent
print(sqrt(2))      #square root
print(cos(0))       #cos(),sin(),tan()
print(pi)           #pi value

print("------------------------------------")

#operators precedence # (),** # *,/ # +,-

print(20-3*4)        # *,-
print((20-3)+2**2)   # (),**,+
print((5*2)+(2**2))  # (),+
print(2*8/2**2)      # **,/,*(right to left)

print("------------------------------------")

#decimal,binary,hexadecimal,octal

print(bin(5))         # decimal to binary
print(oct(7))         # decimal to octal
print(hex(10))        # decimal to hexa
print(int('0b101',2)) # binay to decimal
print(int('0o7',8))   # octal to decimal
print(int('0xA',16))  # hexa to decimal

print("------------------------------------")

#augmented assignment operator

counter = 0
counter += 1     # counter = 1
counter += 1     # counter = 2
counter += 1     # counter = 3
counter += 1     # counter = 4
counter -= 1     # counter = 3
counter *=2      # counter = 6
print(counter)

print("------------------------------------")

#strings

long_string='''WOW     
O O
---'''
print(long_string)          # '''   ''' for more than one line
print(type("hi hello 24!")) # string type

print("------------------------------------")

#string concatenation

print('hi' + 'bye')
print("agnes" + " " + "preethi")
print("agnes" + " preethi")

print("------------------------------------")

#type conversion

print(type(str(19)))        # convert int to str type
print(type(int(str(19))))   # convert int to str type and str to int type

print("------------------------------------")

#escape sequences

abc="it's me"
print(abc)
abc="it\'s \"me\" baby"
print(abc)
abc="\tit's me"
print(abc)
abc="it's me \nbaby"
print(abc)

print("------------------------------------")

#formatted strings

name = "Agnes"
age = 21
print(f'hi {name},i am {age} years old')
print("Hello {}, your balance is {}.".format("Cindy", 50))
print("Hello {0}, your balance is {1}.".format("Cindy", 50))
print("Hello {name}, your balance is {amount}.".format(name="Cindy", amount=50))
print("Hello {0}, your balance is {amount}.".format("Cindy", amount=50))

print("------------------------------------")

#string indexes,slicing [start:stop],[start:stop:stepover]

python = 'I am PYHTON'
         #012345678910
print(python[1:4])    
print(python[1:])
print(python[:])
print(python[1:100])
print(python[-1])
print(python[-4])
print(python[:-3])
print(python[-3:])
print(python[::-1]) 
print(python[::1])
print(python[::-2])
print(python[::2])

print("------------------------------------")

#function and methods

#functions - round(),abs(),print(),int(),str(),len().....

a = "ABCDE"
    #12345
print(len(a))
print(a[0:5])
print(a[0:len(a)])

#methods - upper()(or) capitalize(),lower(),find(),replace()....

letters = "a,b,c,d is an alphabets"
print(letters.upper())
print(letters.capitalize())
print(letters.find(','))             # output will be index value of ,
print(letters.replace('is','are'))
print(letters)                       # immutable

print("------------------------------------")

#lists
#list slicing

#adding things in list

a = ['a','b','c']
print(a)
a = a + ['d']
print(a)
print('--------------------------------------')
amazon_cart = ['notebooks','sunglasses','toys','grapes']
amazon_cart[0] = 'laptops'
new_cart = amazon_cart[0:3]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print('--------------------------------------')
new_cart = amazon_cart
print(new_cart)
print(amazon_cart)
print('--------------------------------------')
new_cart = amazon_cart[:]
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print('--------------------------------------')
new_cart = amazon_cart
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)
print('--------------------------------------')

#matrix

basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
print(basket[0])
print(basket[1])
print(basket[1][0])
print(basket[1][1])
print(basket[1][2])
print(basket[1][1][0]) 
print("------------------------------------")

#listmethods
b = [1,2,3,4,5]
new_b = b.append(6)             #insert a value at end of the list
print(b)
print(new_b)                    #none
print("------------------------------------")
c = [1,2,3,4,5]
c.insert(3,6)                   #insert a value in specified index of the list   
print(c)
print("------------------------------------")
a = [1,2,3,4,5]
a.extend([50,51])               #extend values
print(a)
print("------------------------------------")
d = [1,2,3,4,5]
d.append(100)
print(d)
d.pop()                         #delete the last value of the list
print(d)
d.pop(0)                        #delete the index of the value 
print(d)
print("------------------------------------")
e = [1,2,3,4,5]
e.remove(4)                     #remove the value
print(e)
new_e = e.remove(3)
print(new_e)
print("------------------------------------")
e = [1,2,3,4,5]
new_e = e.pop(2)
print(new_e)
new_e = e.clear()               # clear all values from the list
print(e)
print("------------------------------------")
b = ['a','x','b','c','d','e','d']
b.sort()                        #sort the list
b.reverse()                     #reverse the above sort values 
print(b[::-1])                  #reverse the above reversed values
print(b)
print("------------------------------------")

#ranges

print(range(1,100))
print(range(0,100))

#join() - method

s = '$'
new_s = s.join(['hi','agi','dear'])
print(s)
print(new_s)
print("------------------------------------")
new_s = ' '.join(['hi','agi','dear'])
print(new_s)
print("------------------------------------")

#list unpacking

a,b,c,*other,d = [1,2,3,4,5,6,7,8]    #can remove [] here it will works
print(a)
print(b)
print(c)
print(other)
print(d)
print("------------------------------------")

#dictionaries

dictionary = {
    'a':[1,2,3],
    'b':'hello',
    'c':True
}
print(dictionary['a'])
print(dictionary['a'][1])
print("------------------------------------")
dictionary = {
    'a':[1,2,3],
    'b':'hello',
    'c':True
}
my_list = [
    {
    'a':[1,2,3],
    'b':'hello',
    'c':True
    },
    {
     'a':[4,5,6],
     'b':'hello',
     'c':True
}
]
print(my_list[0]['a'][2])
print(dictionary['a'][1])
print("------------------------------------")
dictionary = {
     123 :[1,2,3],
     True:'hello',
    'c'  :True
}
print(dictionary[123])
print(dictionary[True])
print("------------------------------------")
dictionary = {
     123 :[1,2,3],
     True:'hello',
    'age': 20
}
print(dictionary.update({'ages':55}))   
print(dictionary)      
print("------------------------------------")

#tuples

x,y,z,*other,a =(1,2,3,4,5,6,7,8)
print(x)
print(y)
print(z)
print(other)
print(a)
b = (1,2,3,4,5,5,6,7,8)
print(b.count(5))
print(b.index(3))
print(len(b))
print("------------------------------------")

#set

g = {'santi','rafee','pree','agi','jesus','moni','maria'}
print(g)
print("------------------------------------")
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.difference(set2))
print(set1.discard(5))
print(set1)
print(set1.difference_update(set2))
print(set1)
print("------------------------------------")
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8,9,10}
print(set1.intersection(set2))   # set1 & set2
print(set1.union(set2))          # set1 | set2
print(set1.isdisjoint(set2))
print("------------------------------------")
set1 = {1,2,3}
set2 = {4,5,6,7,8,9,10}
print(set1.isdisjoint(set2))
print("------------------------------------")
ab = {4,5}
abc = {4,5,6,7,8,9,10}
print(ab.issubset(abc))
print(ab.issuperset(abc))
print(abc.issuperset(ab))
print("------------------------------------")
