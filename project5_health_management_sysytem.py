#health management system
#3 clients -harry, rohan and hamad
def getdate():
    import datetime
    return datetime.datetime.now()
client=input("enter the client name\n")
if client == "harry":
   print("what do you want to do ",client)
   print("1.enter  diet data and exercise \n")
   print("2.see diet data and exercise")
   cammand=int(input("enter the answer\n"))
   if cammand==1:
       print("what do you want to log")
       print("1.enter  diet data  \n")
       print("2.enter exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2==1:
           f=open("harry_diet.txt","a")
           date_time=str(getdate())
           diet=input("enter the food\n")
           a=f.write(date_time)

           a = f.write("\n")
           a=f.write(diet)
           a = f.write("\n")
           f.close()
       else :
            f = open("harry_exercise.txt", "a")
            date_time = str(getdate())
            exercise = input("enter the exercise\n")
            a = f.write(date_time)
            a=f.write("\n")
            a = f.write(exercise)
            a = f.write("\n")
            f.close()
   else:
       print("what do you want to see",client)
       print("1.diet data  \n")
       print("2.exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2==1:
           f=open("harry_diet.txt")
           content=f.read()
           print(content)
           f.close()
       else :
           f=open("harry_exercise.txt")
           content=f.read()
           print(content)
           f.close()





if client == "rohan":
   print("what do you want to do ",client)
   print("1.enter  diet data and exercise \n")
   print("2.see diet data and exercise")
   cammand=int(input("enter the answer\n"))
   if cammand==1:
       print("what do you want to log")
       print("1.enter  diet data  \n")
       print("2.enter exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2==1:
           f=open("rohan_diet.txt","a")
           date_time=str(getdate())
           diet=input("enter the food\n")
           a=f.write(date_time)
           a = f.write("\n")
           a=f.write(diet)
           a = f.write("\n")
           f.close()
       else :
            f = open("rohan_exercise.txt", "a")
            date_time = str(getdate())
            exercise = input("enter the exercise\n")
            a = f.write(date_time)
            a=f.write("\n")
            a = f.write(exercise)
            a = f.write("\n")
            f.close()
   else :
       print("what do you want to see", client)
       print("1.diet data  \n")
       print("2.exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2 == 1:
           f = open("rohan_diet.txt")
           content = f.read()
           print(content)
           f.close()
       else:
           f = open("rohan_exercise.txt")
           content = f.read()
           print(content)
           f.close()

if client == "hammad":
   print("what do you want to do ",client)
   print("1.enter  diet data and exercise \n")
   print("2.see diet data and exercise")
   cammand=int(input("enter the answer\n"))
   if cammand==1:
       print("what do you want to log")
       print("1.enter  diet data  \n")
       print("2.enter exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2==1:
           f=open("hammad_diet.txt","a")
           date_time=str(getdate())
           diet=input("enter the food\n")
           a=f.write(date_time)

           a = f.write("\n")
           a=f.write(diet)
           a = f.write("\n")
           f.close()
       else :
            f = open("hammad_exercise.txt", "a")
            date_time = str(getdate())
            exercise = input("enter the exercise\n")
            a = f.write(date_time)
            a=f.write("\n")
            a = f.write(exercise)
            a = f.write("\n")
            f.close()
   else:
       print("what do you want to see", client)
       print("1.diet data  \n")
       print("2.exercise \n")
       cammand2 = int(input("enter the answer\n"))
       if cammand2 == 1:
           f = open("hammad_diet.txt")
           content = f.read()
           print(content)
           f.close()
       else:
           f = open("hammad_exercise.txt")
           content = f.read()
           print(content)
           f.close()