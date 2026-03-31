from collections import Counter


# def validAnagram(s1,s2):
#     l1=len(s1)
#     l2=len(s2)

#     if l1 != l2:
#         return False
    
#     str1=sorted(s1)
#     str2=sorted(s2)


#     if str1 != str2:
#         return False

#     return True



# def validAnagram(s1, s2):
#     print(Counter(s1)  ,"----------",s2)
#     return Counter(s1) == Counter(s2)

# def validAnagram(s1, s2):
#     if len(s1) != len(s2):
#         return False

#     count = {}

#     # Count characters in s1
#     for ch in s1:
#         count[ch] = count.get(ch, 0) + 1

#     # Subtract counts using s2
#     for ch in s2:
#         if ch not in count:
#             return False
#         count[ch] -= 1
#         if count[ch] < 0:
#             return False

#     return True


# str1 = "naman"
# str2 = "amann"
# print(validAnagram(str1, str2))


def validAnagram(s1,s2):
    return sorted(s1) == sorted(s2)

str1 = "naman"
str2="amann"
print(validAnagram(str1,str2))