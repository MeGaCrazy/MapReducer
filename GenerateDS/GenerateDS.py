import random
import string



def GenerateDS():
    # First DataSet is like User_name , User_id, User_HomeCountry
    users_name = ["MeGaCrazy", "Tourist", "Petr",
                  "moejy0viiiiiv", "W4yneb0t",
                  "TakanashiRikka", "izrak",
                  "Um_nik",
                  "anta",
                  "ershov.stanislav", "dotorya",
                  "LHiC",
                  "mnbvmar",
                  "scott_wu",
                  "Zlobober",
                  "ksun48",
                  "fateice",
                  "bmerry", "qwerty787788", "AngryBacon"]

    for x in range(0, 480):
        users_name.append(''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10)))

    users_location = ["EGYPT", "Russia"]

    Countries = ["France", "EGYPT", "Taiwan", "Japan", "Hungary", "Switzerland", "Poland", "Russia", "China",
                 "Canada", "Italy", "Ukraine", "Bulgaria"]
    for x in range(2, len(users_name)):
        users_location.append(random.choice(Countries))

    with open('/mnt/88E0978DE097805C/FCIH/Projects/3rd1-Semeter/OS2-Task2/GenerateDS/Contestants.txt', 'w') as myfile:
        for x in range(0, len(users_name)):
            myfile.write(str(users_name[x]) + "\t" + str(x) + "\t" + str(users_location[x]) + "\n")
        myfile.close()
    print("Contestants DataSets Has Been Generated")
    #####################################################################
    # Second DataSet is like ContestName,Contest_id,User_id,Rate_OfUser,ContestLocation
    contest_name = []
    Contests_Number = 2018
    Contest_General_Name = "ACMICPC"
    for x in range(1975, Contests_Number):
        contest_name.append(Contest_General_Name + str(x))

    with open('/mnt/88E0978DE097805C/FCIH/Projects/3rd1-Semeter/OS2-Task2/GenerateDS/Contests.txt', "w") as myfile:
        for x in range(0, len(contest_name)):
            Contest_Location = str(random.choice(Countries))
            for y in range(0, 50):
                f = random.randint(0, len(users_name))
                tmp_Rate = random.randrange(65, 75)
                Rate = chr(tmp_Rate)
                myfile.write(contest_name[x] + "\t" + str(x) + "\t" + str(f) + "\t" + str(Rate) + "\t" +
                             Contest_Location + "\n")
        myfile.close()
    print("Contests DataSets Has Been Generated")


if __name__ == '__main__':
    GenerateDS()