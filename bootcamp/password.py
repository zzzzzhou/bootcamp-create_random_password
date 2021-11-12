from random import * #无需形参，返回密码文本


def passwd():
    pwlen = input("your password length")
    pwnum = input("number included? y/n")
    pwcap = input("Capital included? y/n")
    pwsymbol = input("symbol included? y/n")
    num = int(pwlen)
    password = []
    strtemp = ""
    if pwnum == 'N' or pwnum == 'n':
        for i in range(num):
            password.append(chr(randint(97, 122)))
    else:
        for i in range(num - 1):
            password.append(chr(randint(97, 122)))
        password.append(str(randint(0, 10)))
    if pwcap == 'Y' or pwcap == 'y':
        password[0] = chr(randint(65, 90))
    if pwsymbol == 'Y' or pwsymbol == 'y':
        password[-2] = chr(randint(33, 47))
    result = "".join(password)
    print("new password is", result)
    return result
