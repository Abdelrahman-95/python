#-------------------------------------------------
#---- Function Packing, Unpacking Arguments ------
#-------------------------------------------------

def my_skills(name,*skills):
    print(f"Welcome Back {name} ")
    count = 1
    for skill in skills:
        print(f"skill({count}) ======> {skill}")
        count += 1

my_skills("Abdelrahman","python","Html","css","JavaScript")
