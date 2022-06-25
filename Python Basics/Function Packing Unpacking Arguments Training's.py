myTubel = ("Html","Css","Js")
mySkils = {"Python":"50%","css":"90%","js":"85$"}

for key,value in mySkils.items():
    count = 1
    print(f"skill'{count}'=====>>{key}=====>>{value}")
    count += 1

def show_skills(name,*skills,**skillsWithProgress):
    print(f"Hello {name}\nskills Without progress is: ")
    for skill in skills:
        print(f"-{skill}")
    print("Skills with progress is: ")
    for skill_key,skill_value in skillsWithProgress.items():
        print(f"-{skill_key} => {skill_value}")

show_skills("abdelrahman",*myTubel,**mySkils)
