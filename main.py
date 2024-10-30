import random
import string
while True:
 inpt=input("choose 1 to encrypt and 2 to decrypt and 0 to stop: ")
 if int(inpt)==0:
    break
 elif int(inpt)==1:
  a=input('enter message to encrypt : ')
  words=a.split()
  lst=[]
  
  for i in words:
      if len(i)>=3:
         char=random.choice(string.ascii_letters)
         char1=random.choice(string.ascii_letters)
         temp=char1+i[1:]+i[0]+char
         lst.append(temp)
         
      else:
         temp1=i[::-1]
         lst.append(temp1)
      res=' '.join(lst)
      print('.\n.\n.\nur encrypted message is : ',res)
  
     
 elif int(inpt)==2:
    a=input('enter the encrypted code: ')
    words=a.split()   
    lst1=[]
    for i in words:
      if len(i)>=3:
         temp=i[-2]+i[1:-2]
         lst1.append(temp)
      else:
         temp1=i[::-1]
         lst1.append(temp1)
    result=' '.join(lst1)
    print('.\n.\n.\ncode decrypted : ',result)
 print('.\n.\n<<created by Momin>>')
