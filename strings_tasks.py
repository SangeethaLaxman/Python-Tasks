# Given a string, return the string made of its first two chars, so the String "Hello" yields "He".
#  If the string is shorter than length 2, 
# return whatever there is, so "X" yields "X", and the empty string "" yields the empty string "".
x=input("Enter the string:")
print(f"First 2 characters of the string \"{x}\" is : {x[:2]}")


# 2.Given a string, return a new string made of 3 copies of the last 2 chars of the original string. 
# The string length will be at least 2.
if len(x)>=2:
    print(f"3 copies of the last 2 characters of the string \"{x}\" is : {x[-2:]*3}")
else:
    print("lngth should be greater than 2")

# 3.Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".
if (len(x)%2==0):
    print(f"First half of the string \"{x}\" is : {x[:len(x)//2]}")
else:
    print("length is not even")


# 4.Given a string, return a version without the first and last char, so "Hello" yields "ell". 
# The string length will be at least 2.

print(f"without the first and the last character of the string \"{x}\" is : {x[1:-1]}")

# 5.Given two strings, a and b, return the result of putting them together in the order abba, e.g. 
# "Hi" and "Bye" returns "HiByeByeHi".
str1=input("Enter string1:")
str2=input("Enter string2:")
str3=str1+str2+str2+str1
print(f"abba string for the strings \"{str1}\" and \"{str2}\" is : {str3}")

# 6.Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty (length 0).
print(len(str1))
if (len(str1)!=len(str2)):

    if (len(str1)>len(str2)):
        str4=str2+str1+str2
    
    elif(len(str1)<len(str2)):
        str4=str1+str2+str1
    
    print(f"short+long+short for \"{str1}\" and \"{str2}\" is : {str4}")
elif(len(str1)==len(str2)):
    print("strings are same length")

# 7.Given 2 strings, return their concatenation, except omit the first char of each. The strings will be at least length 1.

str5=str1+str2
print(f"concatenation without first character for \"{str1}\" and \"{str2}\" is : {str5[1:]}")

# 8.Given a string, return a "rotated left 2" version where the first 2 chars are moved to the end.
#  The string length will be at least 2.
if len(x)>=2:
    print(f"rotated left version of \"{x}\"  is : {x[2:]+x[:2]}")