def duplicate_string(s):
    count = {}

    for char in s:
        if char in count:
            count[char]+=1
        else:
            count[char]=1


    return count;



string = "Python Programming"

print(duplicate_string(string));