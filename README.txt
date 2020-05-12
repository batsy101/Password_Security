After comming across the sight haveibeenpwned and the password and idea of keeping your credentials safe. I, a cyber security aspirant, thought of taking this as an opportunity to put this into work and also get to learn more of the amazing python language.

How to execute the code:

python secure_pwd.py <your password>

-->This python code accepts a password as argument

-->U can enter the characters that you want to accept or deny based on your own policies and standards

-->You can also use the list i have created by default or add values to the list to avoid pain of entering the values every time you execute

-->The first function will check whether your password adheres to the standards of a stron password

-->After successfully verifying this your passwords will now be compared to the list 

--> This is the list of all the passwords that have been pawned in data breaches that have occured so far

--> This list was found in haveibeenpwned.com

--> Since the list is only the hash of all the passwords the pwd you entered will be hashed and compared

--> If your password is already pawned you will recieve a notification else your are safe

Note: the passwords file is named pwd.txt you can change it if you want

To produce test cases for the code .. use the test.py file to generate hash values. Put them in a file and make it your target file.
