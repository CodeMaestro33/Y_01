print("Welcome to my computer quiz")

playing = input("Do you want to play? ")
if playing.lower() != "yes":
    quit()

print("Okay! Let's play the game :) ")
score = 0

answer = input("What does SSD stand for? ")
if answer.lower() == "solid state drive":
    print('Correct')
    score += 1
else:
    print('Incorrect!')

answer = input("What does HDD stand for? ")
if answer.lower() == "hard disk drive":
    print('Correct')
    score += 1
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == "graphical processing unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print('Correct')
    score += 1
else:
    print('Incorrect')

print("You got " + str(score) + " questions correct")
percentage_score = (score / 4) * 100
print("You got " + str(percentage_score) + "%.")