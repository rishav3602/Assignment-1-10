#2. Correct the following code and write the comment where you made the correction?

class_started = int(input("Hey friend, is class started?: [0-False/1-True]"))
# In order to enter 0/1 we will have to type caste it into integer not boolean...

if class_started:
      print("Since class started...")
      print("Lets concentrate")
else:
      print("Since class is not started...")
      print("let's revise")    
