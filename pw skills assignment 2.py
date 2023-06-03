#!/usr/bin/env python
# coding: utf-8
Q1. How do you comment code in Python? What are the different types of comments?

Ans:- comment in the python are identified with a # symbol, and extend to the end of the line .
Hase character in a string are not considered comment how ever there are two ways to write a comments 
1 single line comments
2 multiline comments Q2. What are variables in Python? How do you declare and assign values to variables?

Ans: variable is a contenor which store the any types of value like integer, float and string etc.
For example :
when we declare a variable then we will use assignment operator without assignment operator we can not assign a variable .
example
 
 A = 25
 
 A--- Variable name 
 (=)---Assignment operator 
 (25)--Integer valueQ3. How do you convert one data type to another in Python?
Ans: python defines type conversion function like int(),float() and str() to directly convert one data type to another dataa type.
Example

A = 5.2
B = int(A)
print(B)
print(type(B))Q4. How do you write and execute a Python script from the command line?

To write and execute a Python script from the command line, follow these steps:

1. Open a text editor of your choice (e.g., Notepad, Sublime Text, Visual Studio Code) and create a new file.

2. Write your Python code in the text editor. For example, let's say you want to create a script that prints "Hello, World!":

print("Hello, World!")

3. Save the file with a .py extension. For example, you can save it as hello.py.

4. Open a command line or terminal window on your operating system.

5. Navigate to the directory where you saved the Python script using the cd command. For example, if your script is saved on the         desktop, you can use the following command on Windows:

cd C:\Users\YourUsername\Desktop
cd /Users/YourUsername/Desktop
6.Once you are in the correct directory, you can execute the Python script by typing python followed by the script filename. For example:

python hello.py

7. Press Enter to run the command. The Python interpreter will execute the script, and in this case, it will print "Hello, World!" in the command line.
# In[2]:


#  Q5. Given a list my_list = [1, 2, 3, 4, 5], write the code to slice the list and obtain the sub-list [2, 3].


my_list = [1, 2, 3, 4, 5]

my_list[1:3:1]

Q6. What is a complex number in mathematics, and how is it represented in Python?

Ans: Complex number are the number that are expressed in the form of a + bi where a, b are real number and "i" is a imaginary number.
Example :-

a = 4 + 5i
print(type(a))    
# In[3]:


#   Q7. What is the correct way to declare a variable named age and assign the value 25 to it?
#  Ans:
age = 25
print(age)


# In[8]:


#  Q8. Declare a variable named price and assign the value 9.99 to it. What data type does this variable belong to?
# Ans:
    
price = 9.99
print(price)
print('this variable belong to',type(price))


# In[12]:


#   Q9. Create a variable named name and assign your full name to it as a string. How would you print the value of this variable?
#  Ans:-
name = "Vipin Rajpoot"
print("My Name is",name)


# In[15]:


#  Q10. Given the string "Hello, World!", extract the substring "World".

str1 = "Hello World"
str1[6::]


# In[35]:


#  Q11. Create a variable named "is_student" and assign it a boolean value indicating whether you are currently a student or not.


is_student == True
print('student', True)
is_student == False
print('not student', False)


# In[ ]:




