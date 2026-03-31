def firstUniqueChar(s):
    count = {}
    for ch in s:
        count[ch]=count.get(ch,0)+1

    for c in count:
        if count.get(c,0) == 1:
            return c

    return False
        

   
    


s = "feafgfgtaygegayfetyp"
print(firstUniqueChar(s))