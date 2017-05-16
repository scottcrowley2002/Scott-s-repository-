from time import sleep
score = 0
print("Welcome to a revision maths test!")
print("FIRST WE WILL HAVE A FEW RANDOM QUESTIONS AND THEN SOME MULTIPLICATION,ADDITION,SUBTRACTION AND DIVISION!!!")
answer=input("what is 9x12?")
if answer=="108":
    print("That is correct!")
    score = score + 1
elif answer=="99":
    print("You just left out one nine hard luck!")
else:
    print("Nope,unlucky!The answer is 108")
print("Next question!")
answer=input("what is 2 to the power of 7?")
if answer=="128":   
    print("That is correct!")
    score = score + 1
elif answer=="64":
    print("you forgot to multply the 64 by 2")
else:
    print("no,hard luck!The answer is 128")
print("Time for another question!")
answer=input("What is 20% of 215")
if answer=="43":
    print("Excellent!")
    score = score + 1
elif answer=="41":
    print("Incorrect,but so close")
else:
    print("Incorrect!The answer is 43")
print("Time for another question!")
answer=input("The pattern is 1,7,14,_,28.Fill in the missing blank")
if answer=="21":
    print("Well done")
    score = score +1
elif answer=="20":
    print("Nope!")
else:
    print("Nope the answer is 21")
answer=input("How many sides does a hexagon have?")
if answer=="6":
    print("Well done that's correct!")
    score = score +1
elif answer=="5":
    print("Nope that is incorrect!")
else:
    print("Unlucky!")
answer=input("Is a 90 degrees angle called an obtuse angle?")
if answer=="no":
    print("Yes,well done!")
    score = score +1
elif answer=="yes":
    print("Incorrect!")
else:
    print("Nope,incorrect!")
print("TIME FOR SOME MULTIPLICATION!!!")
answer=input("What is 12x12?")
if answer=="144":
    print("Correct!")
    score = score +1
elif answer=="132":
    print("Incorrect!")
else:
    print("Incorrect!")
answer=input("What is 7x9?")
if answer=="63":
    print("That's correct!")
    score = score +1
elif answer=="54":
    print("Wrong!")
else:
    print("Incorrect!")
answer=input("What is 6x7?")
if answer=="42":
    print("Well done!")
    score = score +1
elif answer=="36":
    print("Unlucky!")
else:
    print("Unlucky!")
answer=input("What is 8x4?")
if answer=="32":
    print("Correct!")
    score = score +1
elif answer=="24":
    print("Incorrect!")
else:
    print("Incorrect!")
answer=input("What's 32x3")
if answer=="96":
    print("Well done!")
    score = score +1
elif answer=="88":
    print("Hard luck!")
else:
    print("Hard luck!")
answer=input("What's 5x11")
if answer=="55":
    print("Correct!")
    score = score +1
elif answer=="44":
    print("Unlucky!")
else:
    print("Unlucky!")
print("TIME FOR SOME ADDITION!!!")
answer=input("What's 45+32")
if answer=="77":
    print("Excellent!")
    score = score +1
elif answer=="73":
    print("Wrong!")
else:
    print("Wrong!")
answer=input("What is 21+49")
if answer=="70":
    print("Well done!")
    score = score +1
elif answer=="71":
    print("Hard luck!")
else:
    print("Hard luck!")
answer=input("What's 99+99")
if answer=="198":
    print("Correct!")
    score = score +1
elif answer=="199":
    print("Incorrect!")
else:
    print("Incorrect!")
print("TIME FOR SOME SUBTRACTION!!!")
answer=input("What is 567-45")
if answer=="522":
    print("Excellent!")
    score = score +1
elif answer=="521":
    print("Wrong!")
else:
    print("Wrong!")
answer=input("What is 1000000-1")
if answer=="999999":
    print("Super!")
    score = score +1
elif answer=="99999":
    print("Unlucky!")
else:
    print("Unlucky!")
print("TIME FOR SOME DIVISION!!!")
answer=input("What's 121 divided by 11?")
if answer=="11":
    print("Excellent!")
    score = score +1
elif answer=="110":
    print("Incorrect!")
else:
    print("Incorrect!")
answer=input("What's 64 divided by 8")
if answer=="8":
    print("Well done!")
    score = score +1
elif answer=="7":
    print("Wrong!")
else:
    print("Wrong!")
answer=input("What is 72 divided by 9?")
if answer=="8":
    print("Excellent!")
    score = score +1
elif answer=="7":
    print("Hard luck!")
else:
    print("Hard luck!")
answer=input("Did you enjoy this test?")
if answer=="yes":
    print("Thank you!")
elif answer=="no":
    print("oh :(")
else:
    print("Awhh too bad")
print("This is the end of the test")
print("Your final score out of 20 questions is "+ str(score))

print("IN PERCENTAGE THIS IS...")
sleep(2.5)
print("CALCULATING...")
sleep(2)
count_to = 100 * (score) / 20
print (str(count_to) +'%')
