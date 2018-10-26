#!/usr/bin/python

class MyClass:

    #Constructor - this function gets invoked automatically when you create
    #an instance of this MyClass
    def __init__(self):
        print('Constructor got invoked')
        self.x = 0
        self.y = 0
        self.result = 0

    def setValues(self,val1,val2):
        self.x = val1
        self.y = val2

    def printValues(self):
        print('First value : ', str(self.x) ) 
        print('Second value : ', str(self.y) ) 

    def addValues(self):
        return self.x + self.y

def main():
    obj = MyClass()
    obj.setValues(100,200)
    obj.printValues()

    print('The result is ' , obj.addValues() )

if __name__ == "__main__":
   main()
        
