class Opp():
    def __init__(self):
        print(
           """
Even and odd Nuber "1" , len string "2" , range loop "3" ,division1 ,"4" , division2 "5" , exit "0" """)
        self.choose =  int(input("Enter the choice: ").strip())
    def even_odd(List:list)->list:
        even_number,odd_number = [],[]
        [even_number.append(number) if number %2 == 0 else odd_number.append(number) for number in List] 
        print(f"{even_number}\n{odd_number}")
    
    def count_word(self):
        Word = str(input("Enter One Word: ").strip())
        Len_Word = len(Word)
        List_Word = Word.split()
        if len(List_Word) > 1: 
            print("Please Enter One Word: ") 
            count_word()
        for W in Word:
            if Word.count(W) > 1:
                Len_Word -=1
        print(f"lens of {Word} is a {Len_Word} ")

    def range_loop(self):
        Number = int(input("Enter Number: ").strip())
        for N in range(0,Number+1): print(N)
    
    def division(self):  
        Number_1 = int(input("Enter Number One: ").strip())
        Number_2 = int(input("Enter Number Two: ").strip())
        Number_3 = []
        Number_4 = []
        for Number in range(1,Number_1+1):
            if Number % Number_2 == 0:
                Number_3.append(Number)
            else:
                Number_4.append(Number)
        print(Number_3)

    def division2(self):  
        Number_1 = int(input("Enter Number One: ").strip())
        Number_2 = int(input("Enter Number Two: ").strip())
        Number_3 = []
        Number_4 = []
        for Number in range(1,101):
            if Number % Number_1 == 0:
                Number_3.append(Number)
            if Number % Number_2 == 0:
                Number_4.append(Number)
        print(Number_3)
        print(Number_4)

    def main(self):
        while True :
            
            if self.choose == 1 :
                return even_odd()
            elif self.choose == 0:
                break
            
Opp()
