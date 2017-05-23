

print(" >>This is a game that you will always get 10 as your answer<<")

print("")

from time import sleep

score=int(input("pick a number higher than 1"))

print("")

print("Multiply your answer by 2")

score = score*2

sleep(5)

print(score)

print("")

print("Multiply your current number by 5")

score = score*5

sleep(5)

print(score)

print("")

print("Divide your current number by your original number")

score = score / score

sleep(5)

print("")

print('Remember at the start I said this game will always give the answer of 10?')

print("")

sleep(2)

print("the final answer is...")

sleep(2)

score = score*10

print(score)
