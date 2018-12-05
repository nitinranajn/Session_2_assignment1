#!/usr/bin/env python
# coding: utf-8

# ## Session 2
# 
# ## Assignment 1 Question
# 
# ## Problem Statement
# 1. Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list.
# 
# 2. Create the below pattern using nested for loop in Python.
# 
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
# 
# 3. Write a Python program to reverse a word after accepting the input from the user.
# Sample Output:
# Input word: AcadGild
# Output: dilGdacA
# 
# 4. Write a Python Program to print the given string in the format specified in the sample
# output.
# WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
# Sample Output:
# WE, THE PEOPLE OF INDIA,
# having solemnly resolved to constitute India into a SOVEREIGN, !
# SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
# and to secure to all its citizens

# In[23]:


## 1. Write a program which accepts a sequence of comma-separated numbers from console and generate a list
#----------------------------------------------------------------------------------------------------------
list=[]
list = input("Please enter the number:")
l = list.split(',')
print("Here is the list you have entered:")

print(l)


# In[24]:


##2. Create the below pattern using nested for loop in Python.

#*
#* *
#* * *
#* * * *
#* * * * *
#* * * *
#* * *
#* *
#*
#----------------------------------------------------------------------------------------------------------
for i in range(6):
    print('* '*i)
for j in range(4, 0, -1):
    print('* '*j)




# In[26]:


#3. Write a Python program to reverse a word after accepting the input from the user.
#Sample Output:
#Input word: AcadGild
#Output: dliGdacA
#----------------------------------------------------------------------------------------------------------
word= input("Enter a word:")

print("output", word[::-1])


# In[26]:


#4. Write a Python Program to print the given string in the format specified in the sample output.
#WE, THE PEOPLE OF INDIA, having solemnly resolved to constitute India into a SOVEREIGN,
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC and to secure to all its citizens
#Sample Output:
#WE, THE PEOPLE OF INDIA,
#having solemnly resolved to constitute India into a SOVEREIGN, !
#SOCIALIST, SECULAR, DEMOCRATIC REPUBLIC
#and to secure to all its citizens 
#-----------------------------------------------------------------------------------------------------------------


print('''WE, THE PEOPLE OF INDIA,\nhaving solemnly resolved to constitute India into a SOVEREIGN, !\nSOCIALIST, SECULAR, DEMOCRATIC REPUBLIC \nand to secure to all its citizens''')


# In[ ]:




