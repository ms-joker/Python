'''
Mehmet Sıddık UYGUROĞLU
May 04, 2021
Chat.py 

Basic Chat program.

'''

import time

print("\n\n");
isim = input("What is your name?");
print(f"Hi {isim}, This name sounds very good!");
time.sleep(2)
yash = int(input(isim + " How old are you? "))

if yash < 10:
    print(" Looks like you are going to middle school.")
elif yash >9 and yash<14:
    print(" Looks like you are going to high school.")
elif yash>13 and yash<18:
    print("Looks like you are goting to university.")
else:
    print("Woops, "+isim+" you are big enough to be my parent. :) ")
