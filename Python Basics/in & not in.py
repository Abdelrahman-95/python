Users = ["Abdelrahman","Mohamed","Mahmoud"]
country = ["Egypt","Ksa","Bahrian"]
course_price = 150

if "Abdelrahman" in Users :
    print(f"Welcome Mr {Users[0]} to Python Course")
    if "Egypt" or "Ksa" in Country:
        print(f"You have a discount {course_price*70/100:.0f}$ from {course_price}$")
    else:
        print("You have not any discount")
elif "mohamed" not in Users:
    print("Welcome To My Course You Have 10% discount")
