import cv2
import os

img=cv2.imread("mypic.jpg")
msg=input("enter secert message")
password=input("enter a passcode")

d={}
c={}

for i in range(255):
    d[chr(i)]=i
    c[i]=chr(i)

n=0;
m=0;
z=0;

for i in range(len(msg)):
    img[n,m,z]=d[msg[i]]
    n=n+1
    m=m+1
    z=(z+1)%3

cv2.imwrite("encryptedimage.jpg",img)
os.startfile("encryptedimage.jpg")

message =""

n=0
m=0
z=0

pas = input("Enter passcode for Decryption")

if password == pas:
    for i in range(len(msg)):
        message = message + c[img[n,m,z]]
        n=n+1
        m=m+1
        z=(z+1) % 3
    print("Decryption message=",message)
else:
    print("Not valid key")
