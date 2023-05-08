import random
#game == random
pc_number=random.randint(1,20)
count=0
while True:
    user_number=int(input("Enter a number: "))
    if user_number==pc_number:
        print("Victoryyyy")
        count+=1
        print("You had : " , count ,"guesses")
        break
    elif user_number<pc_number:
        print("Aim higher...")
        count+=1
    elif user_number>pc_number:
        print("come downnn")
        count+=1
    
