#Day6
#Decision Making

#Comparison Operators
# == Equal to
# |=Not equal to
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less thamn or Equal to

# IF STATEMENT
#if condition:
    #do something

age = 12
if age >= 18:
    print('You can vote')

    #if...else statement
else:
    print("You cannot vote")



    #if...elif...else statement
    score = 90

    if score >= 90:
        print("A")

    elif score >= 80:
        print("B")

    elif score >= 70:
        print("C")

    else:
        print("FAIL")


        #LOGICAL OPERATORS
        # and
        # or
        # Not

age = 20
is_available = False

if age >= 18 and is_available:
    print("You can vote")

else:
    print("You cannot vote")


if age >= 18 or is_available:     
        print("You can vote")
else:
    print("You cannot vote")


if not is_available:
 print("You cannot vote")

else:
    print("You can vote")



    
    

