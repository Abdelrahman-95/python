# ------------------------
# -- Function Recursion --
# ------------------------
# ---------------------------------------------------------------------
# -- To Understand Recursion, You Need to First Understand Recursion --
# ---------------------------------------------------------------------

def cleanWord(word):
    if len(word) == 1:
        return word

    if word[0] == word[1]:
        return cleanWord(word[1:])
    return word[0]+cleanWord(word[1:])
    
    
        
    
print(cleanWord("gggoooaaalll"))
