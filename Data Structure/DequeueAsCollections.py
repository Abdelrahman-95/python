# Import collections module:
import collections

# Initialize deque:
dq = collections.deque()

def DQAdd(Value):
    dq.append(Value)
    
def DQAddL(Value):
    dq.appendleft(Value)
    # print(list(dq)[0])
    
def DQEX(Value):
    dq.extend([Value])
    print(list(dq))
    print(list(dq)[0])

def DQEXL([Value]):
    dq.extendleft[Value])
    print(list(dq)[0])


DQAdd(5)
DQAddL(10)
DQEX(15)
DQEXL(11,13)
