print ("Welcome to my first game!!")

name = input("What is your name? ")
age = int(input("What is your age? "))

hp = 10

if age >= 18:
  print("you are old enough to play :) ")
  
  want_to_play = input("Do you wanna play? (yes/no) ").lower()
  if want_to_play == "yes":
    print("lets go!!!")
    print("you will start with", hp, "hp")
    
    left_or_right = input("do you want to go left or right? (left/right) ")
    if left_or_right == "left":
      ans = input("Nice!..you reached a swamp, do you want go around or across the swamp? (around/across) ")
      
      if ans == "around":
        print("you went around the swamp and gained 1 hp")
        hp += 1
        
      elif ans == "across":
        print("you acrossed the swamp but you were bitten by a snake and lost 5 hp")
        hp -= 5
        
      ans_1 = input("you came across house and river..do you wan to go iside the house or to the river?(house/river) ")
      if ans_1 == "house":
         print("you were hit by a man and lost 5 hp")
         hp -= 5
        
         if hp <= 0:
           print("you have 0 hp and lost :(")

         else:
           print("you survived the game and won :)")
        
      else:
         print("you were drawn in the river and lost :(")

      
    else:
      print("you fell down the hell... you lost :(")
        
  else:
      print ("okay:( ")

else:
  print("you are underage :( ")
