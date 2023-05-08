import random
number_in_list=int(input("Enter the count of the random numbers in the the list: "))
user_list=[]
for i in range (number_in_list):
    n=random.randrange(100000)
    user_list.append(n)
print("Your List: ", user_list)