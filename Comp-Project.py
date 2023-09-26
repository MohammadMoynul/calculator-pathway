#!/usr/bin/env python
# coding: utf-8

# # Group 5

# ## Team Members:

# ### Ekhlasur Rahman

# ### Sufiyan Kazi

# ### Mohammad Hassan Arif

# ### Thang Toan Thong

# ## Date:-23/09/2023

# # This is a program for basic calculator in python

# ## Importing math function

# In[14]:


import math


# ## Declaring variable with intial value of zero 

# In[15]:


operation = 0


# ## Making a while loop and another while loop inside it

# In[16]:


while operation != 7:   # condition for user input
    operation = int(input("Chose the operation to be implied.\
                          \nEnter:1 for Addition\
                          \nEnter:2 for Subtraction\
                          \nEnter:3 for Multiplication\
                          \nEnter:4 for Division\
                          \nEnter:5 for Second power\
                          \nEnter:6 for Square root\
                          \nEnter:7 for Exit\n"))
    
    if operation == 5 or operation == 6 :      # if statement
        num = int(input("Enter the Number: "))    # User input
    elif operation == 1 or operation == 2 or operation == 3 or operation == 4:  
        num1 = int(input("Enter the first number: "))     # User input
        num2 = int(input("Enter the second number: "))    # User input
    elif operation == 7:  # If user chooses to exit
        print("Goodbye")  
    else:                 # For invalid input
        print("Invalid Input")
        
    while operation != 7:    # condition for running the operation chosen by the user
        if operation == 1:   # For Addition
            print("The sum of the two number is: ",num1 + num2)
            break
        elif operation == 2: # For Subtraction
            print("The substraction of the two number is: ",num1 - num2)
            break
        elif operation == 3: # For Multiplication
            print("The product of the two number is: ",num1 * num2)
            break
        elif operation == 4: # For Division
            print("The division of the two number is: ",num1 / num2)
            break
        elif operation == 5: # For Second power
            print("The second power of the number is: ",num ** 2)
            break
        elif operation == 6: # For Square root
            print("The square root of the number is: ",math.sqrt(num))
            break
        
    
                          


# In[ ]:




