import collections
import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase

besar = collections.deque(string.ascii_uppercase)
kecil = collections.deque(string.ascii_lowercase)

cipher = input("chiper = ")
key = int(input("key = "))

besar.rotate(key)
kecil.rotate(key)

besar = ''.join(list(besar))
kecil = ''.join(list(kecil))



print(cipher.translate(str.maketrans(upper, besar)).translate(str.maketrans(lower, kecil)))

