str=input("enter the string")
print(str)
str1=str[::-1]
print("reversed string",str1)
str2=str1.replace('a',"").replace('e',"").replace('i',"").replace('o',"").replace('u',"")
print("replace vowels",str2)
