import time
#python has a built in module to help us with time
# variable for the timer
seconds = int(input("How long should the timer be? (number only):"))

#now we create the actual timer

for i in range(seconds):
    print(str(seconds-i) + " second(s) remain")
    #print("Loading..." + str(seconds - i))
    # or
    #print("Loading...")
    time.sleep(1)

print("TIME IS UP!!!!!") 

#Now we test it
#If you want to have the seconds show in different forms, you can change it. For example: