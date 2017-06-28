"""
  Name     : c6_15_string_manipulation.py
  Book     : Python for Finance (2nd ed.)
  Publisher: Packt Publishing Ltd. 
  Author   : Yuxing Yan
  Date     : 6/6/2017
  email    : yany@canisius.edu
             paulyxy@hotmail.com
"""

string='Hellow World!'

# find the length of the string
n_length=len(string)
print(n_length)

# the number of appearance of letter l
n=string.count('l')     
print(n)	

# find teh locatoin of work of 'World'
loc=string.index("World") 
print(loc) 

# number of spaces
n2=string.count(' ')
print(n2)

print(string[0])     # print the first letter 
print(string[0:1])   # print the first letter (same as above)
print(string[0:3])   # print the first three letters
print(string[:3])    # same as above 
print(string[-3:])   # print the last three letters
print(string[3:])    # ignore the first three 
print(string[:-3])   # except the last three 

