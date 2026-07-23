#LOOPS
#Means Repeat Something

print("today is on Thursday")
#We want to print this 100 times

#TYPES OF LOOPS
  #While lopps
  #For Lopps

#While Loops

#While condition
    #code

cake = 1

#while cake <= 9:
    #print(cake)
    

#FOR LOOPS
#Repeat over a sequence

for numbers in range(7):
    print(numbers)

#RANGE
#range(5) print 0-4
for i in range(5):
    print(1)
for i in range(0,12,4):
    print(i)

for i in range(1,6):
    print(i)


#LOOPING THROUGH STRINGS
for letters in "PYTHON":
    print(letters)


#BREAK
#Used to stop the loop immediately

for i in range (1,11):
    if 1==6:
        break
    print(i)

#CONTINUE
#Skips one iteration

for i in range(1,11):
    if i ==5:
        continue
    print(i)

#PASSWORD CHECKER
password = ""
while password != "12345":
    password = input("enter your password: ")
print("WELCOME")


   
