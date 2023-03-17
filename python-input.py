# Define a function that asks user name and print that name to the console

def name():
  name = input("What is your name?")
  print(f"You have given your name as: {name}")
  print("You have given your name as {}".format(name))
  print("You have given your name as " +name)
  

name()
