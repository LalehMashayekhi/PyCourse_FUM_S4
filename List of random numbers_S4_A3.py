import random
number_in_list=int(input("Enter the number of the elements in your list: "))
user_list=[]
for i in range (number_in_list):
    n=random.randrange(1000)
    if n not in user_list:
        user_list.append(n)
   
print("Your List: ", user_list)
