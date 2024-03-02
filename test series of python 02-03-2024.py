#!/usr/bin/env python
# coding: utf-8

# # Q.1  Converting an Integer into Decimals ?

# In[13]:


from decimal import Decimal
a = 5600
type(a)
b = Decimal(a) # with the help of typecasting method we can change datatype of data . 
type(b)


# # Q.2 Converting an String of Integers into Decimals ?

# In[14]:


from decimal import Decimal
a = '5555'
type(a)
b = Decimal(a)
type(b)


# # Q.3  Reversing a string using an Extended Slicing Technique ? 

# In[20]:


a = "teamindia" # string slicing
print(a[1])
print(a[0])
print(a[2])
print(a[3])
print(a[4])
print(a[1:5])
print(a[:])


# In[27]:


a = "teamindia"
print(a[::-1])


# # Q.4  Counting the number of occurances of a character in a string ?

# In[49]:


a ='karamveer'   
b ='e'
def count(a,b):
    number_of_string_occur = 0
    for i in range(len(a)):
        if(a[i] == b):
           number_of_string_occur = number_of_string_occur + 1
    return number_of_string_occur
str = 'karamveer'
b = 'e'
print(count(str , b))


# # Q.5  Find the maximum and minimum number in a list ?

# In[50]:


a = [1,2,3,4,5,6,7,8]
type(a)


# In[53]:


max(a)


# In[54]:


min(a)


# # Q.6  Find the middle element in a list ? 

# In[115]:


list = [1,2,3,4,5] # in case of total element is odd 
middle_element  = int(len(list)/2)
print(list[middle_element])


# In[124]:


list = [ 1,2 ,3, 4, 5, 6,7,8] # there will be two middle element because total element in list is even 
middle_element_first = int((len(list))/2)
middle_element_second = int((len(list)/2 - 1))
print(list[middle_element_first])
print(list[middle_element_second])


# # Q.7  Converting a list into a string ?

# In[67]:


a = ["manish" , "sikha" , "kirti"]
type(a)
for i in a :
    print(i , end = ",")


# # Q.8  Adding two list elements together ?

# In[73]:


a = [1,2,3,4,5,6]
b = [3,4,5,6,7,8]
def add(a,b):
    return a + b 
c = list(map(add , a, b))
print("addition of two list is = " ,  c)


# # Q.9 Write a program to check given number is even or odd ? 
# 

# In[76]:


a = int(input("enter number "))
if(a%2 == 0 ):
    print("entered number is  even number")
else :
    print("entered number is  odd number")


# # Q.10  Write a program to check given character is a vowel or consonant ? 
# 

# In[80]:


a = input("enter character")
b = ['a' , 'e' , 'i' , 'o' , 'u' , 'A','E','I', 'O' , 'U']
if a in b :
    print("entered character is  vowel  number")
else :
    print("entered number is  consonant number")


# # Q.11 Write a program to count vowels and consonants in the string ?
# 

# In[83]:


a = "manish"
b = ['a' , 'e' , 'i' , 'o' , 'u' , 'A','E','I', 'O' , 'U']
total_vovel = 0
total_consonants = 0
for i in a :
    if i in b:
        total_vovel = total_vovel + 1
    else :
        total_consonants = total_consonants + 1
print(total_vovel)
print(total_consonants)


# # Q.12 Write a program to remove spaces from string without inbuilt function ?

# In[91]:


def remove(string):
    return string.replace(" ", "")
string = ' dont know '
print(remove(string))

