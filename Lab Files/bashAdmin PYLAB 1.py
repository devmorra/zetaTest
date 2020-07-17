import getpass
import hashlib
def getUserPassAndDept():
    username = input("What is your username?: ")
    password = getpass.getpass(prompt='Password?: ')
    department = input("What is your department?: ")
    return username, password, department
def hashString(string):
        string = string.encode('utf-8')
        hashedString = hashlib.md5(string).hexdigest()
        return hashedString
def averageInList(numList):
    sum = 0
    for num in numList:
        sum += num
    avg = sum / len(numList)
    return avg
def reverseNumber(num):
    return -num8
#usr, pwd, dept = getUserPassAndDept()
print(getUserPassAndDept())