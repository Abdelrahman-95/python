name = "Abdelrahman"

def one():
    global name
    name = "Mohamed" 
    print(f"hello mr {name}")

def two():
    name = "Mahmoud"
    print(f"hello mr {name}")


one()
print(f"hello mr {name}")
two()
