#!/usr/bin/env python

import argparse
import re
import hashlib

Allow = []
Deny = []

x = int(raw_input("Enter the number of characters u want to make compulsory: "))
'''if x != int(x):
  print("Pls enter an integer....")
  exit()
'''
y = int(raw_input("Enter the number of charachters u want to restrict: "))
'''if y != int(y):
  print("Pls enter an integer....")
  exit()
'''
for i in range(0, int(x)):
  tmp=raw_input("Enter the character u want to allow: ") 
  Allow.append(tmp)

for j in range(0, int(y)):
  temp=raw_input("Enter the character u want to deny: ")
  Deny.append(temp)

parser = argparse.ArgumentParser()
parser.add_argument("pwd", help="enter your password as the argument")
arg = parser.parse_args()

#Deny = ['<*>,?"~']
#Allow = ['1234567890!@#$%^&*()']

def basic_check(pwd):

  val = True

  if not any(a.isdigit() for a in pwd): 
    print('Password should have at least one numeral') 
    val = False
          
  if not any(b.isupper() for b in pwd): 
    print('Password should have at least one uppercase letter') 
    val = False
	          
  if not any(c.islower() for c in pwd): 
    print('Password should have at least one lowercase letter') 
    val = False
          
  if not any(d in Allow for d in pwd): 
    print('Password should have at least one of the symbols') 
    val = False
	 
  if any(e in Deny for e in pwd):
    print('A character that is not permitted is present')
 
  if val: 
    return val 

def check_pwned(passwd):
  pwd_hash = hashlib.sha224(passwd).hexdigest()
  #print(pwd_hash)

  file1 = open('pwd.txt', 'r') 
  Lines = file1.readlines() 
  
  # Strips the newline character 
  for line in Lines: 
    #print(line.strip())
    if str(line.strip()) == str(pwd_hash):
      print("password has already been pwned") 

  
if len(arg.pwd) > 8:
  print("[*] Good the password is greater that 8 characters")
  print("[*] Checking for basic password according to given previous policies")
  basic_check(arg.pwd)
  print("[*] Congratulations your password is qualified... but is it safe..???")
  print("[*] We are checking if your password has been pawned in any previous data breaches")
  check_pwned(arg.pwd)

'''This code is written by the Suketh Evani a.k.a DorKn8. This is just an idea i got after comming across the website https://haveibeenpwned.com/Passwords and reading the content. As I was trying to deepen my knowledge in python while i came across
this site , I have written this python script. You can try to replicate it in any language you whish to and integrate the passwrd list given. Feel free to test many values and update changes. Thank you and please support and follow me if you liked my work. Thank you'''

