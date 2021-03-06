# -*- coding: utf-8 -*-
"""CMPE346_Week2.ipynb

Automatically generated by Colaboratory.

# Regular Expressions
"""

import re

example = 'Hello World'
print(re.findall('Hello', example))
print(re.findall('Hello|World', example))
print(re.findall('hello|world', example))

example = 'AbcDeF12'

print('All chars: ', re.findall(r'[A-z]', example))
print('Upper-case chars: ', re.findall(r'[A-Z]', example))
print('Lower-case chars: ', re.findall(r'[a-z]', example))
print('Digits chars: ', re.findall(r'[0-9]', example))

print('Number: ', re.findall(r'[0-9]+', example))
print('Number: ', re.findall(r'\d+', example))

example = 'Hello World'
print(re.findall(r'^He', example))
print(re.findall(r'ld$', example))
print(re.findall(r'[^ld]', example))

example = 'abcabc'
print(re.findall(r'abc', example))
print(re.findall(r'abc{2}', example))
print(re.findall(r'(abc){2}', example))

print(re.findall(r'a.c', example))
print(re.findall(r'(abc)+', example))
print(re.findall(r'(abc)?', example))

print(re.findall(r's?he|it', 'she he it they'))

"""## Tokenizer"""

example = 'Welcome to Bilgi University !'
tokens = example.split(' ')
print(tokens)

example = 'Welcome to Bilgi University!'
tokens = example.split(' ')
print(tokens)

formatted_example = example.replace('!', ' !')
tokens = formatted_example.split(' ')
print(tokens)

tokens = re.findall(r'\w+|\S+', example)
print(tokens)

tokens = re.findall(r'\w+', example)
print(tokens)

tokens = re.findall(r'\S', example)
print(tokens)

"""## Email Checker"""

email = 'ozgur.ozdemir@gmail.com'
if re.search(r'@\w+.\w+', email):
  print('The email format is correct')
else:
  print('The email format is incorrect')

email = 'ozgur_ozdemir@gmail.com'
if re.search(r'(\w+[.-_]?)+@\w+.\w+', email):
  print('The email format is correct')
else:
  print('The email format is incorrect')

"""## Phone Checker"""

phone = '5551112233'
if re.search(r'\d{10}', phone):
  print('The phone format is correct')
else:
  print('The phone format is incorrect')

phone = '(555)1112233'
if re.search(r'\(\d{3}\)\d{7}', phone):
  print('The phone format is correct')
else:
  print('The phone format is incorrect')

"""## Date Checker"""

date = '10-10-1955'
if re.search(r'[0-9]+-[0-9]+-19(5[1-9]|[6-9][0-9])', date):
  print(f'The date is later than 1950')
else:
  print(f'The date is earlier than 1950')
