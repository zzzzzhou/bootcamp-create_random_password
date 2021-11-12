from passwordVersion2 import *
from store import *

start = True

while start:
    retornot = input("retrieve(y) or generate new password?(n)")
    if retornot == 'y':
        reID = input("retrieve which ID's password?")
        oldpassword = retrieve("password.csv", reID)
        print("oldpassword of",reID, "is", oldpassword)
    else:
        newpassword = passwd()
        ID = input("what is password ID")
        up = input("update or not(y/n)")
        if up == 'y':
            update("password.csv", newpassword, ID)
    temp = input("continue or finish?(y/n)")
    if temp == 'y':
        continue
    else:
        start = False
        print("program done")
        break