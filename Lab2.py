# While Loop basic working in python
i = 0                           # initialization
while ( i < 5 ) :               # condition check
    print ( i )                 # loop body
    i = i + 1                   # increment within the body
print () 

# Factorial program using while loop
print ( "Factorial Program" )
num = int ( input ( "Enter a positive number:" ) )          # default input as a str
fact = 1
while ( num >= 1 ) :
    fact = fact * num
    num = num - 1
print ( "Factorial:", fact )
print ()

# For loop basic working
# 1. List
color_list = [ "red", "yellow", "blue", "red", "white" ]   
for i in color_list :               # i is a str and it's values are given as color_list[0], color_list[1], ...., color_list[len]               
    print( i )
print ()

# 2. Tuple
fruit_tuple = ( "apple", "mango", "banana", "kiwi", "tomato" )   
for i in fruit_tuple :               
    print( i )
print ()

# 3. String
name_string = "Fahad"   
for i in name_string :        
    print( i )
print ()

# For loop using range() function with List ( same for Tuple and String )
for i in range ( len ( color_list) ) :          # i is an int and it's values are 0, 1, 2, ......., len
    print ( f"{color_list[i]} \t color_list[{i}]" )
print ()

# For loop using range() function with Numbers
# 1. range ( 1 parameter i.e condition only )
for i in range ( 5 ) :                          # for ( i = 0 , i < 5 , i++ )
    print ( i )
print ()

# 2. range ( 2 parameters i.e intialization , condition )
for i in range ( 2, 5 ) :                       # for ( i = 2 , i < 5 , i++ )
    print ( i )
print ()

# 3. range (3 parameters i.e initialization , condition , increment )
for i in range ( 1 , 10 , 2 ) :                 # for ( i = 1 , i < 10 , i = i + 2 )
    print ( i )
print ()

# Loop control statements
# 1. break
for number in range( 1, 10 ) :
    print ( number )
    if ( number == 5 ) :
        break
print()

# 2. continue
for value in [ "I" , "Am" , "Fahad" , "Gulzar" ] :
    if ( value == "Fahad" ) :
        continue
    print( value )
    
# Funtions basic structure
def myName () :                                 # A function always starts with "def" 
    print ( "I am Fahad Gulzar" )


myName()                                        # Function call
print ()

# Function with parameters
# 1. str as parameter
def fullName ( first_name, last_name ) :        # A function with 2 parameters
    print ( f"Your full name is {first_name} {last_name}." )


fullName ( "Ali" , "Akbar" )
fullName ( "Ahsan" , "Alahi" )
fullName ( "Ibrahim" , "Butt")
print ()

# 2. int as parameter
def sum ( num1, num2 ):
    print ( num1 + num2 )


sum ( 10 , 20 )
sum ( 5 , -10 )
print ()

# 3. list as parameter
def listSum( full_list ) :
    sum = 0 
    for index in range ( len ( full_list ) ) :
        sum += full_list[ index ]
    print ( "Sum =", sum )


listSum ( [ 10, 20, 30, 40 ] )
listSum ( [ -1, 1, 0, 3, 4 ] )
listSum ( [ 1 + 2j, 2 + 5j ] )
print ()

# default parameter
def countryName ( country = "Pakistan" ) :
    print ( "Your country is", country )


countryName ( "India" )
countryName ( "Australlia" )
countryName ()
print ()

# return statement in Functions
def findValue ( full_list, value ) :
    for i in range ( len ( full_list ) ) :
        if ( full_list[i] == value ) :
            return i
    return -1


numbers_list = [ 5, 10, 15, 0, 12 , "1" ]
index = findValue ( numbers_list, 1 )
if ( index == -1 ) :
    print ( "Not Found" )
else :
    print ( "Found at index", index )
print ()

# Keyword Arguments
def num3Value ( num1, num2, num3 ) :             # parameters will store value as mentioned in the Function Call
    print ( "Num3 =", num3 )

    
num3Value ( num3 = -1, num2 = 5, num1 = 100 )
num3Value ( num3 = 1000, num2 = 75, num1 = 2 )
print ()

# variable number of parameters
def product ( *numbers ) :
    prod = 1
    for num in numbers :
        prod = prod * num 
    print ( "Product =", prod )

        
product ( 10, 5 )
product ( 1, 2, 12 )
product ( 5, 4, 0)
product ( 10, "* ")
print ()

# Classes basic structure
class Test :
    x = 5
    
obj1 = Test() 
print ( obj1.x )

# __init__ function in classes ( Constructor )
class Person :
    def __init__ ( this, name, age ) :                  # "this or self" is a reference to the object calling
        this.name = name
        this.age = age
        

per1 = Person ( "Ahmed", 19 )                           # here this.name = per1.name also this.age = per1.age
per2 = Person ( "Fahad", 20 )                           # here this.name = per2.name also this.age = per2.age
print ( per1.name, per1.age )
print ( per2.name, per2.age )

# methods in classes
class Person :
    def __init__ ( this, name, age ) :                  # "this or self" is a reference to the object calling
        this.name = name
        this.age = age
        
    def personName ( this ) :
        print ( "Person name is", this.name )

per1 = Person ( "Fahad", 19 )                           # here this.name = per1.name also this.age = per1.age
per1.personName ()

print ( "ok" )
