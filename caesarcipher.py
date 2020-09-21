import collections
import string


def string_rotate(cipher,key):

    upper = string.ascii_uppercase
    lower = string.ascii_lowercase

    besar = collections.deque(string.ascii_uppercase)
    kecil = collections.deque(string.ascii_lowercase)

    key = -key

    besar.rotate(key)
    kecil.rotate(key)

    besar = ''.join(list(besar))
    kecil = ''.join(list(kecil))

    return(cipher.translate(str.maketrans(upper, besar)).translate(str.maketrans(lower, kecil)))


def user_input():
    cipher = input("chiper = ")
    bruteforce(cipher)


def bruteforce(cipher):

    for key in range (26):
        print(key," | ",string_rotate(cipher,key))

user_input()