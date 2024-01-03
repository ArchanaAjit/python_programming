str=input("Enter a string:")  
temp = str  
rev = 0  
while(str > 0):  
    dig = str % 10  
    revrev = rev * 10 + dig  
    number = str // 10  
if(temp == rev):  
   print("This value is a palindrome number!")  
else:  
   print("This value is not a palindrome number!")  
