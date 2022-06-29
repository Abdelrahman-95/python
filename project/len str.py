word = str(input("enter one word: "))
Len_word = len(word)
for i in word:
    if word.count(i)> 1:
        Len_word-=1
print(Len_word)
        
