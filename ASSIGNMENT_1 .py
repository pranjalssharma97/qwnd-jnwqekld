#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#1. In the below elements which of them are values or an expression? eg:- values can be
integer or string and expressions will be mathematical operators.
*
#HELLO
87.8
-
()
+
6


# In[1]:


#ANS1 
#AS IT IS WRITTEN IN QUESTION VALUES CAN BE INTEGER OR STRING, WHEREAS MATHEMATICAL OPERATORS WILL BE TREATED AS EXPRESSIONS.
#   * - IT IS NEITHER A INTEGER NOR A STRING, THEREFORE IT WILL BE TERATED AS MATHEMATICAL OPERATOR AO THEREFORE IT IS AN EXPRESSION.


#  "HELLO" SINCE IT IS A STRING SO IT WILL BE TEATED AS VALUE.

# 87.8 SINCE IT IS AN INTEGER IT WILL BE TERADTED AS VALUE.

# - IT IS A MATHEMATICAL OPERATOR SO IT WILL BE TREATED AS EXPRESSION.

# / IT IS A MATHEMATICAL OPERATOR SO IT WILL BE TAKEN AS EXPRESSION.

# + IT IS A MATHEMATICAL OPERATOR SO IT WILL BE TAKEN AS EXPRESSION

# 6 IT IS AN INTEGER VALUE SO THEREFORE IT WILL BE TREATED AS VALUE.


# In[2]:


#Q.2 2. What is the difference between string and variable?


# In[3]:


#ANS2  STRING IS SOMETHING WHICH WE ASSIGN WITH THE HELP OF VARIABLE. FOR EG. a="10".In this condition a is called as variable and "10"is known as string.
# a STRING is always stored in a temporary memory which is RAM.STRING IS BASICALLY ANY VALUE WHICH IS REPRESENTING TEXT WITH DOUBLE OR SINGLE QOUTES.
#VARIABLE IS A SYMBLIC NAME THAT IS A REFRENCE OR POINTER TO AN OBJECT.


# In[4]:


#Q.3 3. Describe three different data types.


# In[5]:


#ANS.3 1. STRING DATA TYPE= "SUDH", "PRANJAL","123"IT IS A COLLECTION OF ONE OR MORE CHARACTERS PUT IN A SINGLE OR DOUBLE QOUTES.
#STRINGS ARE IMMUTABLE.
#2. TUPLE- IT IS LIKE A LIST BUT NOT EXACTLY LIKE A LIST. IT IS ABLE TO HOLD ELEMENTS.EX= t=(1,2,3). tuple is a immutable collection
# we generally use tuple for protecting the password, when we want that somebody else should not perform any change.

#3. list- l=[1,2,3,4] it is collection of homogenous or hetrogenous data.list is a mutable entity.


# In[6]:


#4.Q.4 What is an expression made up of? What do all expressions do?


# In[7]:


# ANS.4 expressions are made up of mathematical operators. It is a combination of operators and operands.
#An expression is an instruction that combines values and operators and always evaluates down to a single value. 

#all expressions represnts a value. for ex add +, multilply * etc. Any string is also an expressions since it represents the value of the string as well.


# In[8]:


#Q.5 5. This assignment statements, like spam = 10. What is the difference between an
#expression and a statement?


# In[23]:


#ans.5 An expression evaluates to a single value,a statement does not.


# In[2]:


#q.6 6. After running the following code, what does the variable bacon contain?
bacon = 22
bacon + 1


# In[3]:


bacon


# In[4]:


#ans6the value of bacon is 22


# In[5]:


#q.7. What should the values of the following two terms be?
'spam'+'spam'


# In[6]:


'spam'*3


# In[7]:


#ans7 answer have been anwered in the above cell no. 5 and 6.


# In[8]:


#q.8. Why is eggs a valid variable name while 100 is invalid?


# In[10]:


egg="123"


# In[11]:


100="1234"


# In[12]:


#ans 8 we cannot assign integer to save the variable name.  we can use  _100 as the variable name.


# In[13]:


_100="1234"


# In[14]:


_100


# In[18]:


#q.9 What three functions can be used to get the integer, floating-point number, or string
#version of a value?


# In[20]:


#ans9  int() , float() , and str( ) functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.


# In[21]:


#q.10. Why does this expression cause an error? How can you fix it?
#'i have eaten'+99+'burritos'


# In[22]:


"i have eaten"+"99"+"burritos"


# In[ ]:


#ans9 since 99 is not a string so it is not adding up, in order to add all three they should be string, so i have made 99 as string. by using double qoutes.

