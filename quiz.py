print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
	quit()

print("Okay! Let's play :)")
score = 0;

answer = input("what is py stand's for -> ")

if answer == "Python":
	print("CORRECT!!")
else:
   print("WRONG!!")

answer = input("what is RAM stand's for -> ")

if answer == "Random Access Memory":
	print("CORRECT!!")
	score = score + 1
else:
   print("WRONG!!")

answer = input("what is IND stand's for -> ")

if answer == "India":
	print("CORRECT!!")
	score = score + 1
else:
   print("WRONG!!")

answer = input("what is LUV stand's for -> ")

if answer == "I Love You":
	print("CORRECT!!")
	score = score + 1
else:
   print("WRONG!!")

print("Score card -> " + str(score))

print("You got => " + str((score/4) * 100) + "%.")