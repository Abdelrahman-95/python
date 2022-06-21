"""
start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for i in range(start,end+1):
    for y in range(1,11):
        print(f"{i} X {y} = {i*y}")
    print(15*"-")
"""

def multiplication_table(start,end,ms,md):
    for i in range(start,end):
        for y in range(ms,md+1):
            print(f"{i} X {y} = {i*y}")
        print(15*"-")


multiplication_table(1,10,1,9)
