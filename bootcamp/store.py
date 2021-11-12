from pandas import *


def update(filename, pswstr, id):  # 三个形参都是是文本
    temppd = read_csv(filename)
    newpass = {'Password': pswstr, 'ID': id}
    temppd = temppd.append(newpass, ignore_index=True)
    temppd.to_csv(filename, sep=",")
    print("update done!")


def retrieve(filename, ID):  # 形参都是文本
    temppd = read_csv(filename)
    for i in range(len(temppd)):
        if temppd['ID'][i] == ID:
            getpass = temppd['Password'][i]
            break
        else:
            getpass = "no such password found"
    return getpass  # 传回文本，无论是否找到密码
