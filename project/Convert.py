
# Word = input("Enter Text: ")
# Word_List = Word.split()
# Word_1 = "#".join(Word_List)
# Unicode = [104, 101, 108, 108, 35, 109, 114, 35, 97, 98, 100, 111]
# discode = []

def unicode():
    Word = input("Enter Text: ")
    Word_List = Word.split()
    Word_1 = "#".join(Word_List)
    global Unicode
    Unicode = []
    for W in Word_1:
        Unicode.append(ord(W))
    Final_U = str(Unicode)
    print(Final_U)

def decode():
    global decode
    decode = []
    for U in Unicode:
        decode.append(chr(U))
    Final_D = "".join(decode)
    print(Final_D.replace("#"," "))
unicode()
decode()