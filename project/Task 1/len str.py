# word = str(input("enter one word: "))
# Len_word = len(word)
# for i in word:
#     if word.count(i)> 1:
#         Len_word-=1
# print(Len_word)
        
def count_word():
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
        
count_word()