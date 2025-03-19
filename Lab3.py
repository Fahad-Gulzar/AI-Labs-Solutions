# # Ques: 01

# for num in range ( 1500, 2701 ) :
#     if ( num % 7 == 0 and num % 5 == 0 ) :
#         print ( num )
        
# # Ques: 02

# def fahToCel ( f ) :
#     c = ( ( f - 32 ) / 9 ) * 5 
#     print ( f"{f} deg F is {c} deg Celcuis ")
    
# def celToFah ( c ) :
#     f = ( ( c  * 9 ) / 5 ) + 32
#     print ( f"{c} deg C is {f} Fahrenheit ")

# value = int ( input ( "Enter Temperature: ") )
# conversion = int ( input ( "To convert F to C Enter 1 \nTo convert C to F Enter 2 \nEnter Value: " ) )

# if ( conversion == 1 ) :
#     fahToCel ( value )
# elif ( conversion == 2) :
#     celToFah ( value )
# else :
#     print ( "Invalid Entry! Program Ended") 

# Ques: 03

import random
print ( "Guess The Number Game" )
while True :
    prompt_value= int( input ( "Enter Your Guessed Value: " ) )
    if prompt_value == random.randrange( 1 , 10 ) :
        