import string
import random


if __name__ == "__main__":
    s1 = string.ascii_lowercase              #gives lower case letter
    # print(s1)
    s2 = string.ascii_uppercase
    # print(s2)                                #gives  upper case letter
    s3 = string.digits
    # print(s3)                                #give digits
    s4 = string.punctuation                   #gives punctuation
    # print(s4)
while True:
    plen = int(input("Enter password length : "))
    s = []       #empty list
    s.extend(list(s1))               #extend function combines the string and list convert it to list.
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    random.shuffle(s)             #suffles the item of the list
    # print(s)
    print("Your password is : ")                
    print("".join(random.sample(s, plen)))
    # print("".join(s[0:plen]))