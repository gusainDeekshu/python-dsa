def lastWordLength(str):


    trim_str=str.strip()
    l=len(trim_str)

    count=0

    while l > 0:
        l-=1
        if trim_str[l] == ' ':
            # print("loop break")
            break
        else:
            count+=1


    return print(count," is the last word count");

       







string = " is luffy still joyboy ";
lastWordLength(string);