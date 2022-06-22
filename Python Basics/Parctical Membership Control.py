# Admin List
admins = ["Abdelrahman","Mohamed","Ahmed","Ali"]

# Login input Name

name = str(input("Enter Your Login Name: ")).strip().capitalize()

# if Name in Login List

if name in admins :
    print(f"Welcome Back {name}.")
    option = str(input("Deleted or Updated Your Name: ")).strip().capitalize()
    if option == "Updated" or option =="U":
        NewName = str(input("Enter a new name: ")).strip().capitalize()
        admins[admins.index(name)]= NewName
        print(admins)
    elif option == "Deleted" or option =="D":
        admins.remove(name)
        print(admins)

else:
    print("You are't admin. ")
    option = str(input("You want to be admin 'Yes or Not': ").strip().capitalize())
    if option == "Yes" or option == "Y":
        admins.append(name)
        print("Your Name Have Been Added.")
        print(admins)
    elif option == "Not" or option == "N":
        print("Thank You For using my App. Bye!!!")

    else:
        print("Wrong Choice")

        
