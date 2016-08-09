#!/usr/bin/python
# Script to set up basic Django structure

def not_string(str):
    if (str[:4] == "not "):
        return str
    else:
        return "not " + str

def flimflam():

    for num in range(1,100):
        if (num % 3 == 0 and num % 5 ==0):
            print("FLIMFLAM")
        elif (num % 3 == 0):
            print("FLIM")
        elif (num % 5 == 0):
            print("FLAM")
        else:
            print(num)

def no_dupes(arr):
    no_dupes_list = []
    for num in arr:
        if num not in no_dupes_list:
            no_dupes_list.append(num)

    return no_dupes_list

def main():
   
    print (not_string("Hi, this is a string"))
    print (not_string("not a string here"))
    print (not_string("nothing stange about this one"))
    flimflam()
    x = [ 1, 4, 2, 7, 3, 1, 2, 8 ]
    x = list(no_dupes(x))    
    print(x)
    y = [ 100, 32, 44, 44, 23, 32, 44 ]
    y = list(no_dupes(y))
    print(y)

if __name__ == '__main__':
    main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
