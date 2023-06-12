print("Welcome to my python Quiz")

playing = input(" Do you want to play? ")

if playing != "Yes":
    quit()

print("Ok! Lets Play :)")

answer = input("What is my last name? ")
if answer == "karuthodiyil":
    print('Correct!')
else:
    print("Incorrect!")
