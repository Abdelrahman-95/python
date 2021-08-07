q = [4,5,4]

# Queue Append
def QAdd(Value):
    q.insert(-1,Value )
    Value =( input("Ender value wnat to be add in Queue: ") )
    index = q.index(Value)
    Len   = len(q)
    if index == 0:
        print(f"you add '{Value}' to the Queue and you are nuber 1 in the Queue ")
    else :   
        print(f"you add {Value} to queue  and you waiting {index+1} element ")   
        print(f"you are number {Len} in the Queue")
    print(q[0])
# Queue Remove  
def QRM():
    
    if len(q) != 0:
        q.remove(q[0])
        print(q[0],"removed from the Queue")
    else:
        print("Queue is empty you can't remove anything")
        pass
    

while True:
    print("append: '1', remove: '2', size: '3', is clear: '4', quit '5'  ")
    choice = int(input("Enter Your choice : "))
    if choice == 1:
        QAdd()
        
    if choice == 2 :
        QRM()
        
         
    if choice ==  5 :
        print("you finsh to adding and removing with queue ")
        break
    