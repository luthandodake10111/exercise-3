#Question 1: Basic Function Definition and Calling
#TODO1
def greet(name):
    print("Hello World!")

#_______________________________________________________________________
#Question 2: Function with Parameter
#TODO2
def personalized_greeting (name):
    print(f"Hello {name} how are you doing bro?")
personalized_greeting("Luthando")

#_________________________________________________________________________
#Question 3: Function with Return Value
#TODO3
def square(number, area):
    area= number*area
    print("area")

#def square(number):
    #return number*number
    #print(number**2)


#TODO4
#print the result
print(square(5))
#_________________________________________________________________________
#Question 4: Function with Multiple Parameters and Return Value
#TODO5
def rectangle_area(length,width):
    area = length*width
    print(area)

#TODO6
def rectangle_area(length, width):
    area = length*width

print(rectangle_area(4,5))

#________________________________________________________________________
#Question 5: Using a Function as an Argument
#TODO7
def apply_operation(function,number):
    return function(number)         #parametes= function then number

#TODDO8
def double(number):
    return number *2  #double or (number + number)

#TODO9
def apply_operation(double,number):
    number= 7
    print(apply_operation(double,7))

#TODO10
def apply_operation(square,number):
    number= 3
    print(apply_operation(square, 3))
    

