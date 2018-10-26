#!/usr/bin/python

def getInputs():
    num1 = input('Enter your first number :')
    num2 = input('Enter your second number :')

    return num1,num2

def printInputs(val1,val2):
    print ('First value : ' + str(val1) )
    print ('Second value : ' + str(val2) )

def addValues(val1,val2):
    return val1+val2

def printResult(x,y,result):
    print ('The sum of ' + str(x) + ' and ' + str(y) + ' is ' + str(result) )

def main():
    x,y = getInputs()
    printInputs( x, y )
    printResult( x, y, addValues(x,y) )

main()
