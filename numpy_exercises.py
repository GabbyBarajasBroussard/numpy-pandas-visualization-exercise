#!/usr/bin/env python
# coding: utf-8

# In your numpy-pandas-visualization-exercises repo, create a file named numpy_exercises.py for this exercise.
# 
# Use the following code for the questions below:

# In[2]:


import numpy as np


# In[3]:


a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])


# 1. How many negative numbers are there?

# In[4]:


# First I want to see which numbers are negative
neg_num = a < 0
# Now I am counting each negative number
sum_neg_num= np.count_nonzero(a < 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are", sum_neg_num, "negative numbers in this numpy array.")


# 2. How many positive numbers are there?

# In[12]:


# First I want to see which numbers are positive
pos_num = a > 0
# Now I am counting each positive number
sum_pos_num= np.count_nonzero(a > 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are", sum_pos_num, "positive numbers in this numpy array.")


# 3. How many even positive numbers are there?

# In[15]:


get_ipython().run_cell_magic('time', '', '##How many even positive numbers are there?\n#First I want to isolate my even numbers and my positive numbers\neven_num = a % 2 == 0\n#Now I want to count values that are both even and positive\nsum_pos_evens= np.count_nonzero(pos_num & even_num)\n# If I was presenting the outcome to the user, this is what I would want to print.\nprint("There are", sum_pos_evens, "positive even numbers in this numpy array.")')


# 4. If you were to add 3 to each data point, how many positive numbers would there be?

# In[11]:


## If you were to add 3 to each data point, how many positive numbers would there be?
#First, I want to add 3 to each data point
add_three= a + 3
# Finding the amount of positive numbers after three has been added to each data point.
sum_pos_plus_three= np.count_nonzero( add_three > 0)
# If I was presenting the outcome to the user, this is what I would want to print.
print("There are",sum_pos_plus_three, "positive numbers in this new numpy array.")


# 5. If you squared each number, what would the new mean and standard deviation be?

# In[17]:


# First I would square the array
squared_num= np.square(a)
#Now I would want to calculate the new standard deviation.
stddev= squared_num.std()
# If I was presenting the outcome to the user, this is what I would want to print.
print("The new standard deviation of the array is", stddev)


#Finally, I would calculate the new mean of the array.
mean= squared_num.sum() / 12
# If I was presenting the outcome to the user, this is what I would want to print.
print("The new mean of the array is", mean)


# 6. A common statistical operation on a dataset is centering. This means to adjust the data such that the mean of the data is 0. This is done by subtracting the mean from each data point. Center the data set. See this link for more on centering.

# In[25]:


#First I want to calculate the mean of the original array.
mean = a.mean()
# If I was presenting the outcome to the user, I would want to show them the mean I calculated.
print("The mean of the original array is", int(mean), ".")
## Now I want to set up my equation to center the array
centered= a - int(mean)
# If I was presenting the outcome to the user, this is what I would want to print.
print("The centered array is", centered)


# 7. Calculate the z-score for each data point. Recall that the z-score is given by:
# 
# $ Z = x −μσ $

# In[36]:


#First I am going to calculate the standard deviation of the array
stddev= a.std()
# If I was presenting the outcome to the user, this is what I would want to print to show that I calculated the standard deviation properly.
print("The standard deviation of the array is", stddev)
#Because I am tired, I am going to just reuse the mean from the last problem in my z score function.
z_score= (a-mean)/stddev
# If I was presenting the outcome to the user, this is what I would want to print.
print("The z score for each value in the array is", z_score)


# Copy the setup and exercise directions from More Numpy Practice into your numpy_exercises.py and add your solutions.

# In[42]:


# Life w/o numpy to life with numpy

## Setup 1
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a = np.array(a)
# Use python's built in functionality/operators to determine the following:


# In[45]:


# Exercise 1 - Make a variable called sum_of_a to hold the sum of all the numbers in above list
sum_of_a= a.sum()
sum_of_a


# In[48]:


# Exercise 2 - Make a variable named min_of_a to hold the minimum of all the numbers in the above list
min_of_a= a.min()
min_of_a


# In[49]:


# Exercise 3 - Make a variable named max_of_a to hold the max number of all the numbers in the above list
max_of_a=a.max()
max_of_a


# In[51]:


# Exercise 4 - Make a variable named mean_of_a to hold the average of all the numbers in the above list
mean_of_a= a.mean()
mean_of_a


# In[54]:


# Exercise 5 Make a variable named product_of_a to hold the product of multiplying all the numbers in the above list together
product_of_a= np.prod(a)
product_of_a


# In[56]:


# Exercise 6 - Make a variable named squares_of_a. It should hold each number in a squared like [1, 4, 9, 16, 25...]
squares_of_a= np.square(a)
squares_of_a


# In[57]:


# Exercise 7 - Make a variable named odds_in_a. It should hold only the odd numbers
odds_in_a= a[a % 2 ==1]
odds_in_a


# In[ ]:


# Exercise 8 - Make a variable named evens_in_a. It should hold only the evens.


# In[58]:


evens_in_a= a[a % 2 ==0]
evens_in_a


# In[68]:


## What about life in two dimensions? A list of lists is matrix, a table, a spreadsheet, a chessboard...
## Setup 2: Consider what it would take to find the sum, min, max, average, sum, product, and list of squares for this list of two lists.
b = [
    [3, 4, 5],
    [6, 7, 8]
]
b= np.array(b)


# In[72]:


# Exercise 1 - refactor the following to use numpy. 
# Use sum_of_b as the variable. **
# Hint, you'll first need to make sure that the "b" variable is a numpy array**
sum_of_b = 0
for row in b:
    sum_of_b += sum(row)  


# In[73]:


sum_of_b= np.sum(b)   
sum_of_b


# In[ ]:


# Exercise 2 - refactor the following to use numpy. 
min_of_b = min(b[0]) if min(b[0]) <= min(b[1]) else min(b[1])  


# In[74]:


min_of_b= np.min(b)
min_of_b


# In[ ]:


# Exercise 3 - refactor the following maximum calculation to find the answer with numpy.
max_of_b = max(b[0]) if max(b[0]) >= max(b[1]) else max(b[1])


# In[76]:


max_of_b= np.max(b)
max_of_b


# In[ ]:


# Exercise 4 - refactor the following using numpy to find the mean of b
mean_of_b = (sum(b[0]) + sum(b[1])) / (len(b[0]) + len(b[1]))


# In[79]:


mean_of_b= b.mean()
mean_of_b


# In[ ]:


# Exercise 5 - refactor the following to use numpy for calculating the product of all numbers multiplied together.
product_of_b = 1
for row in b:
    for number in row:
        product_of_b *= number


# In[80]:


product_of_b= np.product(b)
product_of_b


# In[ ]:


# Exercise 6 - refactor the following to use numpy to find the list of squares 
squares_of_b = []
for row in b:
    for number in row:
        squares_of_b.append(number**2)


# In[81]:


squares_of_b= np.square(b)
squares_of_b


# In[ ]:


# Exercise 7 - refactor using numpy to determine the odds_in_b
odds_in_b = []
for row in b:
    for number in row:
        if(number % 2 != 0):
            odds_in_b.append(number)


# In[82]:


odds_in_b=b[b % 2 ==1]
odds_in_b


# In[ ]:


# Exercise 8 - refactor the following to use numpy to filter only the even numbers
evens_in_b = []
for row in b:
    for number in row:
        if(number % 2 == 0):
            evens_in_b.append(number)


# In[83]:


evens_in_b=b[b % 2 ==0]
evens_in_b


# In[ ]:


# Exercise 9 - print out the shape of the array b.


# In[87]:


b.shape


# In[ ]:


# Exercise 10 - transpose the array b.


# In[86]:


np.transpose(b)


# In[ ]:


# Exercise 11 - reshape the array b to be a single list of 6 numbers. (1 x 6)


# In[89]:


np.concatenate(b)


# In[ ]:


# Exercise 12 - reshape the array b to be a list of 6 lists, each containing only 1 number (6 x 1)


# In[94]:


b.reshape(1, 6).T


# In[99]:


## Setup 3
c = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# HINT, you'll first need to make sure that the "c" variable is a numpy array prior to using numpy array methods.
c= np.array(c)


# In[101]:


# Exercise 1 - Find the min, max, sum, and product of c.
np.min(c)


# In[102]:


np.max(c)


# In[103]:


np.sum(c)


# In[104]:


np.product(c)


# In[ ]:


# Exercise 2 - Determine the standard deviation of c.


# In[106]:


c.std()


# In[ ]:


# Exercise 3 - Determine the variance of c.


# In[107]:


np.var(c)


# In[ ]:


# Exercise 4 - Print out the shape of the array c


# In[108]:


c.shape


# In[ ]:


# Exercise 5 - Transpose c and print out transposed result.


# In[109]:


np.transpose(c)


# In[ ]:


# Exercise 6 - Get the dot product of the array c with c. 


# In[110]:


np.dot(c,c)


# In[ ]:


# Exercise 7 - Write the code necessary to sum up the result of c times c transposed. Answer should be 261


# In[117]:


np.sum(c*np.transpose(c))


# In[118]:


# Exercise 8 - Write the code necessary to determine the product of c times c transposed. Answer should be 131681894400.
np.product(c*np.transpose(c))


# In[120]:


## Setup 4
d = [
    [90, 30, 45, 0, 120, 180],
    [45, -90, -30, 270, 90, 0],
    [60, 45, -45, 90, -45, 180]
]
d= np.array(d)


# In[121]:


# Exercise 1 - Find the sine of all the numbers in d
np.sin(d)


# In[123]:


# Exercise 2 - Find the cosine of all the numbers in d
np.cos(d)


# In[124]:


# Exercise 3 - Find the tangent of all the numbers in d
np.tan(d)


# In[126]:


# Exercise 4 - Find all the negative numbers in d
d[d < 0]


# In[127]:


# Exercise 5 - Find all the positive numbers in d
d[d > 0]


# In[128]:


# Exercise 6 - Return an array of only the unique numbers in d.
np.unique(d)


# In[129]:


# Exercise 7 - Determine how many unique numbers there are in d.
len(np.unique(d))


# In[130]:


# Exercise 8 - Print out the shape of d.
d.shape


# In[132]:


# Exercise 9 - Transpose and then print out the shape of d.
d_transposed= np.transpose(d)
d_transposed.shape


# In[133]:


# Exercise 10 - Reshape d into an array of 9 x 2
d.reshape(9,2)


# Awesome Bonus For much more practice with numpy, Go to https://github.com/rougier/numpy-100 and click the "Fork" icon in the upper-right of the screen to fork the repo. This makes a copy of the repo onto your own account. Next, clone your fork https://github.com/your-username/numpy-100 down to your machine. Work through, add, commit, and push your solutions to your own repo.
