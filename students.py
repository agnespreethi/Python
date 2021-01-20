for i in range(0,2):
    name=input('Enter the name')
    age=input('Enter the age')
    id=input('Enter the ID')

class Student():
    def detail(self):
        print('name is: '+name)
        print('age is: '+age)
        print('ID is: '+id)

for i in range(0,2):
    s=Student()
    s.detail()
print("-------------------------------")


list1=[1,2,3,4,5]

def multi(num):
    result=num*2
    return result

print(list(map(multi,list1)))


        
    
