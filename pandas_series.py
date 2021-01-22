#!/usr/bin/env python
# coding: utf-8

# # 1. Use pandas to create a Series from the following data:

# In[36]:


import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


fruits= ["kiwi", "mango", "strawberry", "pineapple", "gala apple", "honeycrisp apple", "tomato", "watermelon", "honeydew", "kiwi", "kiwi", "kiwi", "mango", "blueberry", "blackberry", "gooseberry", "papaya"]


# A. Name the variable that holds the series fruits.

# In[4]:


fruits = pd.Series(fruits)


# B. Run .describe() on the series to see what describe returns for a series of strings.

# In[6]:


fruits.describe()


# C. Run the code necessary to produce only the unique fruit names.

# In[7]:


fruits.unique()


# D. Determine how many times each value occurs in the series.

# In[9]:


fruits.value_counts()


# E. Determine the most frequently occurring fruit name from the series.

# In[10]:


fruits.mode()


# F. Determine the least frequently occurring fruit name from the series.

# In[ ]:


fruits.value_counts().nsmallest(keep='all')


# G. Write the code to get the longest string from the fruits series.

# In[11]:


fruits.apply(len).idxmax()


# H. Find the fruit(s) with 5 or more letters in the name.

# In[12]:


fruits[fruits.str.len() >= 5]


# I. Capitalize all the fruit strings in the series.

# In[13]:


fruits.str.capitalize()


# J. Count the letter "a" in all the fruits (use string vectorization)

# In[65]:


fruits.str.count("a").sum()


# K. Output the number of vowels in each and every fruit.

# In[44]:


fruits[fruits.str.count('[aeiou]')]


# L. Use the .apply method and a lambda function to find the fruit(s) containing two or more "o" letters in the name.

# In[16]:


fruits[fruits.apply(lambda fruit: fruit.count('o') >=2)]


# M. Write the code to get only the fruits containing "berry" in the name

# In[17]:


fruits[fruits.str.contains('berry')]


# N. Write the code to get only the fruits containing "apple" in the name

# In[18]:


fruits[fruits.str.contains('apple')]


# O. Which fruit has the highest amount of vowels?

# In[19]:


fruits[max(fruits.str.count('[aeiou]'))]


# # 2. Use pandas to create a Series from the following data:

# In[23]:


money=['$796,459.41', '$278.60', '$482,571.67', '$4,503,915.98', '$2,121,418.3', '$1,260,813.3', '$87,231.01', '$1,509,175.45', '$4,138,548.00', '$2,848,913.80', '$594,715.39', '$4,789,988.17', '$4,513,644.5', '$3,191,059.97', '$1,758,712.24', '$4,338,283.54', '$4,738,303.38', '$2,791,759.67', '$769,681.94', '$452,650.23']


# In[24]:


money= pd.Series(money)


# A. What is the data type of the series?

# In[25]:


money.dtype


# B. Use series operations to convert the series to a numeric data type.

# In[27]:


#First I will remove the $
money= money.str.replace("$", "")
#Now I will remove the ,
money= money.str.replace(",","")
#Finally I will convert object to a string
money = money.astype(float)
money


# In[29]:


money.dtype


# C. What is the maximum value? The minimum?

# In[30]:


money.max()


# In[31]:


money.min()


# D. Bin the data into 4 equally sized intervals and show how many values fall into each bin.

# In[32]:


money_bins = pd.cut(money, 4)
money_bins.value_counts()


# E. Plot a histogram of the data. Be sure to include a title and axis labels.

# In[138]:


plt.title("Money Histogram")
plt.xlabel("Money in Hundred Thousands")
plt.ylabel("Count Values")
plt.hist(money, color="cadetblue")
plt.show()


# # 3. Use pandas to create a Series from the following exam scores:

# In[78]:


exam_scores= [60, 86, 75, 62, 93, 71, 60, 83, 95, 78, 65, 72, 69, 81, 96, 80, 85, 92, 82, 78]
exam_scores= pd.Series(exam_scores)


# A. What is the minimum exam score? The max, mean, median?

# In[51]:


exam_scores.min()


# In[52]:


exam_scores.max()


# In[53]:


exam_scores.median()


# B. Plot a histogram of the scores.

# In[54]:


plt.hist(exam_scores, color="cadetblue")
plt.title("Scores")
plt.xlabel("Actual Score")
plt.ylabel("Count of scores")
plt.show()


# C. Convert each of the numbers above into a letter grade. For example, 86 should be a 'B' and 95 should be an 'A'.

# In[56]:


def get_letter_grade (num):
    if num >= 90:
        return "A"
    elif num >= 80 and num <= 89:
        return "B"
    elif num >= 76 and num <= 79:
        return "C"
    elif num >= 70 and num <=75:
        return "D"
    elif num <= 60:
        return "D"
exam_scores.apply(get_letter_grade).sapm


# D. Write the code necessary to implement a curve. I.e. that grade closest to 100 should be converted to a 100, and that many points should be given to every other score as well.

# In[71]:


#finding the amount of the curve by subracting the max score from 100.
curve_amount= 100-exam_scores.max()
curve_amount


# In[80]:


#adding the curve to the scores
exam_scores += curve_amount
exam_scores


# # 4. Use pandas to create a Series from the following string:

# In[87]:


letters=list('hnvidduckkqxwymbimkccexbkmqygkxoyndmcxnwqarhyffsjpsrabtjzsypmzadfavyrnndndvswreauxovncxtwzpwejilzjrmmbbgbyxvjtewqthafnbkqplarokkyydtubbmnexoypulzwfhqvckdpqtpoppzqrmcvhhpwgjwupgzhiofohawytlsiyecuproguy')
letters= pd.Series(letters)


# What is the most frequently occuring letter?

# In[88]:


letters[max(letters.value_counts())]


#  Least frequently occuring?

# In[89]:


letters[min(letters.value_counts())]


# How many vowels are in the list?

# In[94]:


letters.str.count('[aeiou]').sum()


# How many consonants are in the list?

# In[97]:


letters.value_counts().sum()-letters.str.count('[aeiou]').sum()


# Create a series that has all of the same letters, but uppercased

# In[92]:


letters.str.upper()


# Create a bar plot of the frequencies of the 6 most frequently occuring letters.

# In[101]:


most_freq = letters.value_counts().head(6)
plt.title('6 Most Frequently Occuring Letters Graph')
plt.xlabel('Letter')
plt.ylabel('Frequency')
x = most_freq.index
y = most_freq
plt.bar(x,y, color='cadetblue')


# # 5. 17 list comprehension problems using Pandas

# In[103]:


fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits= pd.Series(fruits)
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
numbers= pd.Series(numbers)


# Exercise 1 - rewrite the above example code using list comprehension syntax. Make a variable named uppercased_fruits to hold the output of the list comprehension. Output should be ['MANGO', 'KIWI', etc...]

# In[104]:


fruits.str.upper()


# Exercise 2 - create a variable named capitalized_fruits and use list comprehension syntax to produce output like ['Mango', 'Kiwi', 'Strawberry', etc...]

# In[105]:


fruits.str.capitalize()


# Exercise 3 - Use a list comprehension to make a variable named fruits_with_more_than_two_vowels. Hint: You'll need a way to check if something is a vowel.

# In[113]:


fruits[fruits.str.count('[aeiou]') > 2]


# Exercise 4 - make a variable named fruits_with_only_two_vowels. The result should be ['mango', 'kiwi', 'strawberry']

# In[114]:


fruits[fruits.str.count('[aeiou]') == 2]


# Exercise 5 - make a list that contains each fruit with more than 5 characters

# In[115]:


fruits[fruits.str.len() > 5]


# Exercise 6 - make a list that contains each fruit with exactly 5 characters

# In[116]:


fruits[fruits.str.len() == 5]


# Exercise 7 - Make a list that contains fruits that have less than 5 characters

# In[117]:


fruits[fruits.str.len() < 5]


# Exercise 8 - Make a list containing the number of characters in each fruit. Output would be [5, 4, 10, etc... ]

# In[119]:


fruits.str.len()


# Exercise 9 - Make a variable named fruits_with_letter_a that contains a list of only the fruits that contain the letter "a"

# In[120]:


fruits[fruits.apply(lambda fruit: fruit.count('a') >=1)]


# Exercise 10 - Make a variable named even_numbers that holds only the even numbers 

# In[122]:


numbers[numbers.apply(lambda number: number% 2 ==0)]


# Exercise 11 - Make a variable named odd_numbers that holds only the odd numbers

# In[123]:


numbers[numbers.apply(lambda number: number % 2 ==1)]


# Exercise 12 - Make a variable named positive_numbers that holds only the positive numbers

# In[124]:


numbers[numbers.apply(lambda number: number > 0)]


# Exercise 13 - Make a variable named negative_numbers that holds only the negative numbers

# In[125]:


numbers[numbers.apply(lambda number: number < 0)]


# Exercise 14 - use a list comprehension w/ a conditional in order to produce a list of numbers with 2 or more numerals

# In[127]:


numbers[numbers.apply(lambda number: number > 9)]


# Exercise 15 - Make a variable named numbers_squared that contains the numbers list with each element squared. Output is [4, 9, 16, etc...]

# In[132]:


numbers**2


# Exercise 16 - Make a variable named odd_negative_numbers that contains only the numbers that are both odd and negative.

# In[131]:


numbers[(numbers < 0) & (numbers % 2 == 1)]


# Exercise 17 - Make a variable named numbers_plus_5. In it, return a list containing each number plus five. 

# In[134]:


numbers+5


# BONUS Make a variable named "primes" that is a list containing the prime numbers in the numbers list. *Hint* you may want to make or find a helper function that determines if a given number is prime or not.
