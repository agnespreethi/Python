model=input('Enter the model')
wheel=input('Enter the wheel')
tyre=input('Enter the tyre')
color=input('Enter the color')

class Car():
    x=5
    def __init__(self,model,wheel,x):
        self.model=model
        self.wheel=wheel
        
    

    def features(self,tyre,color):
        self.tyre=tyre
        self.color=color


c1=Car(model,wheel,Car.x)
c1.features(tyre,color)



print(Car.x)
        
