#------------------------------------------------------
#---- Function Packing Unpacking Keyword Arguments ----
#------------------------------------------------------
Dict = {"Python":90}

def add_skills():
    skill = str(input("Enter Your Skill: ").strip().capitalize())
    Parcent = int(input("Enter The Percentage: ").strip())
    Dict = {skill:Parcent}
    print(Dict)
    
def remove_skills():
    Del_Skill = str(input("Enter Your skill for Remove: ").strip().capitalize())
    print(Dict)
    del Dict[Del_Skill]
    print(Dict)
    
remove_skills()
