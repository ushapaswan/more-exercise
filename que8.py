# def encrypt():
#   message = input("Enter the message you want to encrypt")
#   ascii_message = [ord(char)+3 for char in message]
#   encrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(encrypt_message))


# def decrypt():
#   message = input("Enter the message you want to decrypt")
#   ascii_message = [ord(char)-3 for char in message]
#   decrypt_message = [ chr(char) for char in ascii_message]  
#   print (''.join(decrypt_message))

# flag = True
# while flag == True:
#   choice = input("What do you want to do? \n1. Encrypt a message 2. Decrypt a message \nEnter E or D respectively!")
#   if choice == 'e':
#     encrypt()
#   else:
#     choice =='d'
#     decrypt()    
#   play_again = input("Do you want to try agian or Do you want to exit? (Y/N)")
#   if play_again == 'Y':
#     continue
#   elif play_again == 'N':
#     break 


# def a(n,p=10):
#   print("my",n,"and","my",p)
# a("amit",45)
# a("neha")  

# def my_function(name):
#   p=name
#   def my_function2():
#     print(p)
#   my_function2()

# my_function("riya")




    

# list=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# i=0
# a=list[0]
# b=list[0]
# while i<len(list):
#     if list[i]>a:
#         a=list[i]
#         if list[i]<b:
#             b=list[i]
#     i=i+1
# print("maximum number",a)
# print("minimum number",b)


# ls=[[0],[1,3],[5,7],[9,1],[1,1,1]]
# i=0
# sum=0
# while i<len(ls):
#   j=0
#   while j<len(ls[i]):
#       sum=ls[i]+ls[i][j]
#       j=j+1
#   i=i+1
# print(sum)
# print(sum)
# list1=[[0],[1,3],[5,7],[9,11],[13,15,17]]
# list2=[]
# i=0
# while i<len(list1):
#   j=0
#   while j<len(list1[i]):
#     if type (i)==list:
#       print(list1[i])
#       j=j+1
#   i=i+1


# n=[1,2,4]
# i=0
# sum
# while i<len(n):
#   if type(n[i])==list:
#     sum=sum+n[i]
#   i=i+1
# print(sum)

  
 # ls=[[0],[1,3],[5,7],[9,1,5],[21,13,11]]
# i=0
# n=[]
# while i<len(ls):
#   j=0
#   while j<len(ls[i]):
#     n.append (ls[i][j])
#     j=j+1
#   i=i+1
# print((n))
# k=0
# a=n[k]
# while k<len(n):
#   if n[k]>a:
#     a=n[k]
#   k=k+1
# print(a)

# def my_func(a):
#   def my_fun():
#     print("helle"+a)
#   my_fun()
# my_func("usha")

# def my_func(a):
#   def my_fun():
#     i=0
#     while i<10:
#       i=i+1
#       if i%2==0:
#         print(i,"even")
#       else:
#         print(i,"odd")
#   my_fun()
# my_func(1)











# a=[2,4,5,7,8]
# i=0
# sum=0
# b=a[i]
# c=a[i]
# while i<len(a):
#   if a[i]>b:
#     n=a[i]
#     if a[i]<c:``
#       c=a[i]
#     sum=sum+b
#   i=i+1
# avg=sum/11
# print(c)
# print(b)
# print(sum)
# print(avg)


# i=0
# while i<=15:
#   j=1
#   while j<=5:
#     j=j+1
#   print(i+j)


# i=1
# j=2
# while i<16:
#   print()
#   i=i+1
#   break
  
 

# n=[1,2,3,[4,5],[7,9,0]]
# b=[]
# i=0
# while i<len(n):
#   b.append (n[i])
#   j=0
#   while j<len(n[i]):
    # b.append(n[i][j])
    


# num=int(input("enter the num"))
# n=["q","z"]
# k=list(n)
# i=0
# b=[]
# j=1
# while j<=num:
#   i=0
#   while i<len(n):
#     n[i]=k[i]+str(j)
#     b.append(n[i])
#     i=i+1
#   j=j+1
# print(b)