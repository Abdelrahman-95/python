"""
start = int(input("Enter Start: "))
end = int(input("Enter End: "))

for i in range(start,end+1):
    for y in range(1,11):
        print(f"{i} X {y} = {i*y}")
    print(15*"-")
"""
"""
def multiplication_table(start,end,ms,md):
    for i in range(start,end+1):
        for y in range(ms,md+1):
            print(f"{i} X {y} = {i*y}")
        print(15*"-")


multiplication_table(1,5,1,15)
"""

class Multiplication_Table:
    def __init__(self):
        pass

    def multiplacation(self,start,end):
        for i in range(start,end+1):
            for y in range(1,11):
                print(f"{i} X {y} = {i*y}")
            print(15*"-")

m = Multiplication_Table()
m.multiplacation(1,5)
