# for loop to print each friend in the list
friend_list = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hannah", "Ivy", "Jack"]
for item in friend_list:
    print(item)

# for loop to print the first 3 friends in the list
for i in range(3):
    print(friend_list[i])


# for loop to print friends from index 2 to 8 (2 inclusive, 9 exclusive) with an increment of 1
for i in range(2,9,1):
    print(friend_list[i])


# if

score = 60

if score > 90:
  print("gets grade A")
elif score > 69:
  print("gets grade B")
else:
  print("gets grade C")


students_name = ["Alex","Bryan","Christ","Dave","Eva"]
print(students_name)
students_score = [100,75,80,78,65]
print(students_score)
students_grade = []


for i in students_score:
   if i >= 90:
      students_grade.append("A")
   elif i >= 70:
      students_grade.append("B")
   else:
      students_grade.append("C")
print(students_grade)


while True:
   answer = input("""Do you want to loop this argument?
Type yes or no: """)
   if answer.lower() == "yes":
      print("Okey let's go!")
   else:
      print("Good byee...")
      break
   
name = ['josh', 'james', 'joe', 'jim']
        
[print(i) for i in name]

score = 90
print('A') if score >= 90 else print('B') if score >= 80 else print('C')
    

[students_grade.append("A") if(i >= 90) else students_grade.append("B") if (i >= 70) else students_grade.append("C") for i in students_score]
print(students_grade)


import random

score = 0
player_name = input("Please enter your name : ")

while True:
    words = ["python", "computer", "programming","condition", "else", "break", "input","print", "while", "for"]
    pick = random.choice(words)
    random_word = random.sample(pick, len(pick))
    jumbled = "".join(random_word)
    print("Jumbled word is :", jumbled)
    answer = input("what is in your mind? :")
    if answer == pick:
        score += 1
        print("Your score is :", score)
        if score == 10:
            print("Congratulation ",player_name , "you win!")
            print("Your score is :", score)
            break
        else:
            print("Better luck next time... correct word is :", pick)
            cont = input("press 'y' to continue and 'n' to quit : ")
        if cont == "n":
            print(player_name, "Your score is :",score)
            print("Thanks for playing...")
            break