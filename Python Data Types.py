#!/usr/bin/env python
# coding: utf-8

# # Python Data Types
1) Numeric 
    i) integer
    ii) floating point
    iii) complex numbers
2) Strings
    i) Concatenation
    ii) Slicing
    iii) Repetition
3) Tuple
4) List
5) Set
6) Dictionary

# # 1) Numeric

#    ### i) Integer

# * An integer is a non fraction number that can be positve, negative and zero.
# * In python language integer is represented as a data type 'int'
# * there is no limit on how long the integer value is
# 
#   * int class tells the program that the given information/data is in integer from and act accordingly 
#         *FOR EXAMPLE 'int' SHOWS THAT WE CAN PERFOM NUMERIC OPERATIONS ON THIS DATA, 
#         *NUMERIC OPERATION COULD BE +, -, x, OR /

# In[1]:


print(124)


# In[2]:


print(193898938493974)


# In[3]:


print(10000000000000 + 124)


# In[4]:


print(1000000000000000000000000000000000000000000000000000000000000000000000000000000 + 1)


# In[12]:


type(10)


# * In Python Integers are represented by **'int'** class

# * Python can handle a platheora of integers (ofcourse it depends on the system memory)

# ### ii) Floating Point Numbers

# ****A float or floating point is a number with a decimal point****
#    * **Examples include 1.22,0.100,-9.8, -.19.98, 0.000001345 etc**
#    * **float tells the program that a given piece of information belongs to 'float' class and it has values with decimal point**
#    
# **Very small or very large values are often represented in scientific notation (e or E)**

# In[6]:


print(1.29)


# In[7]:


print(-11.98)


# In[8]:


print(-0.99924)


# In[9]:


print(0.123 - 0.0134)


# In[11]:


print(0.08984932481098091858798259138401924097859822034839418388798798347242439847 + 1)


# In[81]:


print(1.2e8)


# In[82]:


print(0.000000000000901920981821)


# In[85]:


print(1.2e-3)


# In[88]:


print(0.000000000000000000167)  # Charge on an electron/proton 


# In[92]:


print(3e8)                     # Speed of light


# In[14]:


type(3.1415)


# **In Python floating point numbers are represented by the class 'float'**

# ### iii) Complex Number

# ****Complex numbers are numbers that contain both real part and imaginary part****
# * **Examples include 8+3j where 8 is a real part and 3j is an imaginary part**
# * **Other examples include 1-5j, -1-2j, -23+33j etc**

# In[19]:


print(8+3j)


# In[20]:


print(1-5j)


# In[21]:


print(-1-2j)


# In[22]:


print(-23+33j)


# In[23]:


type(8+3j)


# * In python complex numbers are represented by the class 'complex' as shown above

# ## 2) String

# ****String is a data type used to represent text data****
#                     * OR *
# * **We can say it is a sequence of characters**
# 
# 
# * ***There can be one or more characters in a string with signle quotation, double quotation and even triple quotation marks***
# 
# 

# In[24]:


print('a')


# In[25]:


print("a")


# In[27]:


print('''a''')


# In[31]:


print("Hello Class!")


# In[93]:


print('My name is Sahibzada Salman, and I am your Artificial Intelligence instructor')


# In[34]:


print('''So this is what a string is, it is a sequence of characters under the quotation marks. The characters can be anything ranging from simple letters to some strange looking charaters like / or  * or & or ^ or % etc''')


# In[35]:


type('This is a string class :)')


# * **In Python, the string is repsented by a class 'str'**
# 
# * **Strings are IMMUTABLE means we cannot change the items in a string**

# #### Operations in String

# ##### We can Perform Concatenation, Slicing and Repetition in Strings 

# #### i) Concatenation

# * **Concatenation means joing two strings together**
# 
# * *let's conocatenate two different strings together* 

# In[39]:


print('Hello Class, ' + 'this is an example of concatenation in strings!')


# In[43]:


print('So, basically we are ' + 'just adding two different strings here using a "+" operator')


# In[98]:


print('Hello '  +  'World!')


# **This is how you can join two different strings**

# #### ii) Slicing 

# **Slicing means cutting a string into different parts**
# 
#    **OR**
#      
# **Extracting different parts of a string**

# In[44]:


print('LANGUAGE')


# * *There are 8 different characters in this word*
# * *So let's extract the 3rd, 4th and the 5th letter from the string which are N, G and U*

# In[47]:


print('LANGUAGE'[2:5])


# #####  You Must Be Wondering Why Did We Selected The Range From [2:5], While We Wanted To Select The 3rd, 4th And The 5th Letter? It Should Have Been From [3:5]?

# **ANS:** **Because in Python the indexing starts from 0**
# 
# *or*
# 
# **We Can Say that Python Starts its counting from '0' not '1' :)**

# In[48]:


print('LANGUAGE'[0])


# In[49]:


print('LANGUAGE'[1])


# In[52]:


print('LANGUAGE'[2])


# In[53]:


print('LANGUAGE'[3])


# In[54]:


print('LANGUAGE'[4])


# In[55]:


print('LANGUAGE'[5])


# In[56]:


print('LANGUAGE'[6])


# In[57]:


print('LANGUAGE'[7])


# **There are 8 characters in this string, but the last character is on no 7 position, becuase python starts counting from 0**

# #####  iii) Repetition

# **Repetition means repeating a sequence or a string a certain number of times**

# In[60]:


print('GO '*2)


# In[61]:


print('GO '*4)


# In[62]:


print('Hey '*5)


# In[63]:


print('etc. '*10)


# ##### 

# ## 3) List  

# **List is a collection of different elements or items inside square brackets '[This, is, a, list, :)]' separated by commas**
# 
# **A list can have elements of the same data type or even elemets of different types for example, a signle list can have integers, float and string items**
# 
# **List  **

# In[2]:


print([1,2,3,4,5,6,7,8,9,10])  # a List of Integers


# In[3]:


print([1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,10]) # a list of floating point numbers


# In[4]:


print([1+2j, -1+2j, -1-2j, 1-2j, -3-3j, 5-6j]) # a list of complex numbers 


# In[5]:


print(['This', 'is', 'a', 'string', 'list']) # a list of strings


# In[7]:


print([1, 10, 100, 1.2, 2.3, 3.4, 1+1j, 2+2j, 3+3j, 'A list can have a combination of all the data types that we discussed'])


# 
# * **A list is MUTABLE, means we can change items in the list by simply using the slicing method (indexing)**
# 
# * *Let's see an example below*

# In[8]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'])


# **There are 8 items in this list, let's access each element one by one**

# In[9]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][0])


# In[10]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][1])


# In[11]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][2])


# In[12]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][3])


# In[13]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][4])


# In[14]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][5])


# In[15]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][6])


# In[16]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][7])


# **Let's access first 3 items at the same time**

# In[17]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][0:3]) 


# **Now, let's access the last 3 items from the list**

# In[18]:


print([1,2,-3, -4, 2.3, -4.5, 1+3j, 'string'][4:7])


# ***We can also replace an element in the list***

# In[32]:


listt = [1,2,-3, -4, 2.3, -4.5, 1+3j, 'string']
print(listt[0:7])


# In[34]:


listt[3] = "replacing the previously placed element (-4) with this sentence :p"
print(listt)


# In[35]:


type(listt)


# ****In Python a list is represented by a "list" class****

# ## 4) Tuple

# **A tuple is a data type used to store multiple items in a single variable**
# 
# ***A tuple is a collection of items which are ordered and unchangable***
# 
# ****The only differnece between a tuple and a list is that lists are mutable while tuples are not****
# 
# 
# **Tuples are identified by paranthesis ()**

# In[36]:


print((1,2.3,1-3j,'This is an example of tuple'))


# In[37]:


type((1,2.3,1-3j,'This is an example of tuple'))


# **We can only access the items in a tuple but not change/replace**

# In[38]:


print((1,2.3,1-3j,'This is an example of tuple')[0])


# In[39]:


print((1,2.3,1-3j,'This is an example of tuple')[1])


# In[40]:


print((1,2.3,1-3j,'This is an example of tuple')[2])


# In[41]:


print((1,2.3,1-3j,'This is an example of tuple')[3])


# In[42]:


print((1,2.3,1-3j,'This is an example of tuple')[0:2])


# In[44]:


print((1,2.3,1-3j,'This is an example of tuple')[2:4])


# ## 5) Sets

# **A set is an unordered collection of items**
# 
# **A set can contain only UNIQUE items means no repetition of the same element**
# 
# **There is no indexing in Sets as all the items are unordered and are unique**
# 
# **A set is MUTABLE means items cannot be changed**
# 
# ***A Set is identified/represented by curly braceks or braces { }***

# In[46]:


print({3,1.22,2.3,3+5j, "this is a set"})


# ****Note that our set of different items was unordered but Python knew that it's a set so it automatically ****

# In[49]:


print({1,1,1,3,3,-6,-7,-8,-8,9,-9,10,11.11,12.2,12.3,15,13.9,'This is an example of tuple'})


# **Note that we had repeated items in the above example but since it was a set, so Python automatically removed them**

# In[51]:


print({1,2.3,1-3j,'There is no indexing in the SETS'}[0])


# In[54]:


type({1,2.3,1-3j,'There is no indexing in the SETS'})


# **In Python sets are represented by the class "set"**

# ## 6) Dictionary

# *****Dictionary is a data type used to store values in key:value pairs*****
# 
# ****Dictionaries are ordered, changable and do not allow duplicates****
# 
# * **Dictionaries are optimized to retrieve values when a key is known**
# * *In key:value, value is the actual information associated with a key, think of it as, items in your room are values, your door is the key and together we call it a room (dic)*
# 
#     * ****things in your room are values****
#     * ****door of your room is the key****
#     * ****together they make a room which is a dictionary****
#     
#     
# *****Each key-value pair is separated by a 'colon :', whereas each key is separated by a 'comma ,'*****

# In[55]:


print({1:'Look', 2:'closely', 3:'You see the difference?'})


# **In above example 1,2, and 3 are the keys, while 'look', 'closely' and 'You see the difference?' are the values assosciated with these keys**

# ****To access an item in the list we look at their keys****

# In[71]:


dictt = {1:'Look', 2:'closely', 3:'You see the difference?'}
print(dictt[1])


# In[72]:


print(dictt[2])


# In[73]:


print(dictt[3])


# **We cannot use values to access the key :p**

# In[74]:


print(dictt['Look'])


# *****We can also update a dictionary with new items*****

# In[75]:


dictt[4] = 'New item'
print(dictt)


# ****We can also replace an item from a dictionary with another item****

# In[76]:


print(dictt, '            This is before replacement')
dictt[3] = 'Replaced item'
print(dictt, '            This is after replacement')


# In[79]:


print(dictt[1:3])


# ***There is no slicing in the dictionaries as shown in the above example***

# In[80]:


type(dictt)


# ****In Python the dictionaries are represented by the class 'dict'**** **as shown above**
