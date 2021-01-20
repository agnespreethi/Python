#basic-1 exercises

#type conversionn (Age calculator - input get from user)

birth_year = input("what year you were born?")
age = 2020 - int(birth_year)
print(f'your age is {age}')

o=input()

#password checker

username = input("Enter Username:")
password = input("Enter Password:")
print(f'{username}, your password {password} is {len(password)} letters lengh')

password_length = len(password)
hidden_password = '*' * password_length
print(f'{username}, your password {hidden_password} is {password_length} letters lengh')

o=input()

#list

basket = ["Banana", ["Apples", ["Oranges"], "Blueberries"]];
print(basket[1][1][0])
print(basket[1][1])

o=input()

basket = ["Banana", "Apples", "Oranges", "Blueberries"];

basket.remove("Banana")              # 1. Remove the Banana from the list

basket.remove("Blueberries")         # 2. Remove "Blueberries" from the list.

basket.append("Kiwi")                # 3. Put "Kiwi" at the end of the list.

basket.insert(0,"Apples")            # 4. Add "Apples" at the beginning of the list

print(basket.count("Apples"))        # 5. Count how many apples in the basket

basket.clear()                       # 6. empty the basket

print(basket)

o=input()

#fix this code so that it prints a sorted list of all of our friends (alphabetical). Scroll to see answer
friends = ['Simon', 'Patty', 'Joy', 'Carrie', 'Amira', 'Chu']
friends.append('Stanley')
friends.sort()
print(friends)

o=input()

#dictionary

user = {
  'age':22,
  'username':'pree',
  'weapons':[1,2,3],
  'is_active':True,
  'clan':'india' 
}                    #1 Create a user profile for your new game. This user profile will be stored in a dictionary with keys:'age', 'username', 'weapons', 'is_active' and 'clan'             

print(user.keys())   #2 iterate and print all the keys in the above user.

user['weapons'].append(4)
print(user)          #3 Add a new weapon to your user

user.update({'is_banned': False}) 
print(user)          #4 Add a new key to include 'is_banned'. Set it to false

user['is_banned'] = True
print(user)          #5 Ban the user by setting the previous key to True

user2 = user.copy()
user2.update({'age': 100, 'username': 'Timbo'})
print(user2)          #6 create a new user2 my copying the previous user and update the age value and username value. 

o=input()

#set

# You are working for the school Principal. We have a database of school students:
school = {'Bobby','Tammy','Jammy','Sally','Danny'}

#during class, the teachers take attendance and compile it into a list. 
attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']

print(school.difference(attendance_list))  #using what you learned about sets, create a piece of code that the school principal can use to immediately find out who missed class so they can call the parents. (Imagine if the list had 1000s of students. The principal can use the lists generated by the teachers + the school database to use python and make his/her job easier): Find the students that miss class!

o=input()

#basic-2 exercises
#counter - compiler

my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item        # 0 + 1,1 + 2,3 + 3,...... = 55
print(counter)
print("------------------------------------------")
my_list = [1,2,3,4,5,6,7,8,9,10]

counter = 0
for item in my_list:
    counter = counter + item        # 1,3,6,10,15,21,28,36,45,55      
    print(counter)
print("-----------------------------------------")
my_list = [1,2,3,4,5,6,7,8,9,10]

for item in my_list:
    counter = 0                     # every time counter = 0
    counter = counter + item        # 10
print(counter)
print("----------------------------------------")

# GUI

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


for image in picture:
  for pixel in image:
    if (pixel == 1):
      print('*', end ="")
    else:
      print(' ', end ="")
  print('')
print("----------------------------------------")

# Find Duplicates

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
print("----------------------------------------")

# Functions

#1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age. 
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?
def checkDriverAge():
    age = input("What is your age?: ")
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()

#2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
#checkDriverAge(92);
#it returns "Powering On. Enjoy the ride!"
#also make it so that the default age is set to 0 if no argument is given.
def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too yound to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")
checkDriverAge()
checkDriverAge(22)
print("----------------------------------------")

# print highet value from the list

def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
  return max(evens)

print(highest_even([10,1,2,3,4,8]))  #max value
print("----------------------------------------")
def highest_even(li):
  evens = []
  for item in li:
    if item % 2 == 0:
      evens.append(item)
    return max(evens)

print(highest_even([2,10,1,2,3,4,8])) # 1st even value
print("----------------------------------------")

#scope - nonlocal keyword

def outer():
    x = "local"               # step2:nonloacl assign 1st x=local
    def inner():
        nonlocal x            # step1:1st action 
        x = "nonlocal"        # step3:assign x value local to nonlocal
        print("inner:", x)    # step4:print
    inner()
    print("outer:", x)        #step5
outer()
print("----------------------------------------")
def outer():
    x = "local"               # step3:assign x value nonlocal to local  
    def inner():
        x = "nonlocal"        #step1:assign x=nonlocal
        print("inner:", x)    #step2
    inner()
    print("outer:", x)        #step4
outer()
print("----------------------------------------")