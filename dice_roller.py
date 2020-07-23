import random as rd

def main():
  #roll = 5
  dice_rolls = 2
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = rd.randint(1, 6)
    dice_sum += roll
    print("You rolled a " + str(roll))
    print('You have rolled a total of ' + str(dice_sum))

if __name__== "__main__":
  main()