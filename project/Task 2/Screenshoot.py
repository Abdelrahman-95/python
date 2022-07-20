import os 
import datetime
import time

login_name = os.getlogin()
path = f"c:\\Users\\{login_name}\\Downloads"
os.chdir(path)
try:
    os.mkdir("ScreenShoot")
except FileExistsError :
    print("Folder ScreenShot is already Exists")
    pass
count = 1
Number_ScreenShoot  = int(input("Enter how many screenshots? ").strip())
M_Or_S = str(input("Enter the time, in minutes or Secounds, between each shot? ,choose Minutes 'M' Or Secounds 'S'? ").strip().title())
if M_Or_S == "Minutes" or M_Or_S == "M":
    Minutes_ScreenShoot = int(input("Enter the time, in minutes, between each shot? ").strip())
elif M_Or_S == "Secounds" or M_Or_S == "S":
    Secounds_ScreenShoot = int(input("Enter the time, in Secounds, between each shot? ").strip())
   


for s in range(Number_ScreenShoot):
    now = datetime.datetime.now()
    current_time = now.strftime("%H.%M.%S")
    print(current_time)
    os.system(f"nircmd.exe savescreenshot ScreenShoot\{current_time}.png")
    count +=1
    time.sleep(Minutes_ScreenShoot*60)

# Name_ScreenShoot    = str(input("Enter the name of the ScreenShoot? ").strip().capitalize())


# def inputs():
#     Number_ScreenShoot  = int(input("Enter how many screenshots? ").strip())
#     Minutes_ScreenShoot = int(input("Enter the time, in minutes, between each shot? ").strip())
#     Name_ScreenShoot    = str(input("Enter the name of the ScreenShoot? ").strip().capitalize())
    
# def screenshots():
#     login_name = os.getlogin()
#     path = f"c:\\Users\\{login_name}\\Downloads"
#     try:
#         os.chdir(path)
    

