#!usr/bin/env python
import hashlib

pwd_hash = hashlib.sha224("Imbatman@23").hexdigest()
print(pwd_hash)

file1 = open('pwd.txt', 'r') 
Lines = file1.readlines() 
  
# Strips the newline character 
for line in Lines: 
  #print(line.strip())
  if str(line.strip()) == str(pwd_hash):
    print("password has already been pwned") 
  
