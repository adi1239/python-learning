# This code validates the username entered by the user by checking the local database

#create the database

db=["John","Dave","Scott","Peter"]

def validate():
  username= input("Enter the Username")
  
  if username in db:
      print("Username is present in our Database")
      
  else:
      userinput=str(input("Username is not present in our Database. \n Do you want to add the Username to the Database? Press Y to add."))
      if userinput == "Y":
          db.append(username)
          print("Username added successfully to the Database. Bye!")
          return 0
          
      else:
          print("There is no proper input from the user. Not adding to the Database. Bye!")
          return 0
    
  
  


validate()
print(db)
