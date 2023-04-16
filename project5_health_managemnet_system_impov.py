#health management system
#3 clients -harry, rohan and hamad

class client:
    def __init__(self,name,age,height,weight,gender):
        self.name=name
        self.age=age
        self.height=height
        self.weight=weight
        self.gender=gender
    pass
    def createfiles(self):
        self.exercise_data=open(f"{self.name}_exercise.text",'w')
        self.diet_data=open(f"{self.name}_diet.text",'w')
    pass
def getdate():
    import datetime
    return datetime.datetime.now()
command2=0
def data_logging(client_name):
    print("what do you want to log")
    print("1. diet data  \n")
    print("2.exercise \n")

    cammand2 = int(input("enter the answer\n"))
    if cammand2 == 1:
        f = open(f"{client_name}_diet.txt", "a")
        date_time = str(getdate())
        diet = input("enter the food\n")
        a = f.write(date_time)

        a = f.write("\n")
        a = f.write(diet)
        a = f.write("\n")
        f.close()
    else:
        f = open(f"{client_name}_exercise.txt", "a")
        date_time = str(getdate())
        exercise = input("enter the exercise\n")
        a = f.write(date_time)
        a = f.write("\n")
        a = f.write(exercise)
        a = f.write("\n")
        f.close()


    return


def data_traversing(client_name):
    print("what do you want to see", client_name)
    print("1.diet data  \n")
    print("2.exercise \n")

    cammand2 = int(input("enter the answer\n"))
    if cammand2 == 1:
        f = open(f"{client_name}_diet.txt")
        content = f.read()
        print(content)
        f.close()
    else:
        f = open(f"{client_name}_exercise.txt")
        content = f.read()
        print(content)
        f.close()

    return


response=0
while(response!=3):
    print("hey you,what do you want to do ")
    print("1.add client details\n")
    print("2.log previously saved clients exercise and diet \n")
    print("3.exit")
    response = int(input("enter the answer \n"))
    if (response == 1):
        name = input("enter clients name \n")
        age = input("enter client's age \n")
        height = input("enter clients height \n")
        weight = input("enter clients weight \n")
        gender = input("enter clients gender \n")
        client1 = client(name, age, height, weight, gender)
        client1.createfiles()
        f = open(f"{client1.name}_exercise.text", 'a')
        details =f"name of client={name} age of client ={age}  gender of client={gender}"
        a = f.write(details)
        f = open(f"{client1.name}_diet.text", 'a')
        a = f.write(details)
        a = f.write("\n")
        f.close()
    elif(response==2):

        client_name=input("enter the name of the client \n")
        print("what do you want to do ", client_name)
        print("1.enter  diet data and exercise \n")
        print("2.see diet data and exercise")

        cammand = int(input("enter the answer\n"))
        if cammand == 1:
            data_logging(client_name)

        else:
            data_traversing(client_name)

